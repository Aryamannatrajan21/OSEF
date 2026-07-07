import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typer.testing import CliRunner
from osef.cli.main import app
from osef.epe.output.sarif import SarifSerializer
from osef.epe.output.junit import JunitSerializer
from osef.epe.core.result import Finding, Provenance, Evidence, Recommendation, AutoFix
from osef.epe.core.severity import Severity
from osef.epe.core.category import Category

runner = CliRunner()


def _get_sample_findings():
    return [
        Finding(
            id="test-finding-1",
            title="Test Rule Violation",
            description="A sample architectural policy violation.",
            severity=Severity.HIGH,
            category=Category.ARCHITECTURE
            if hasattr(Category, "ARCHITECTURE")
            else "Architecture",  # type: ignore
            confidence=0.9,
            provenance=Provenance(
                rule_id="ARCH-001", rule_version="1.0.0", policy_version="1.0.0"
            ),
            evidence=Evidence(
                description="Found direct controller to DB dependency.",
                affected_nodes=["src/controllers/user.py"],
            ),
            recommendation=Recommendation(
                action="Refactor", description="Use a repository pattern."
            ),
            autofix=AutoFix(available=False),
        )
    ]


def test_sarif_serializer():
    findings = _get_sample_findings()
    sarif_str = SarifSerializer.serialize(findings)
    data = json.loads(sarif_str)
    assert data["version"] == "2.1.0"
    assert "runs" in data
    assert len(data["runs"]) == 1
    run = data["runs"][0]
    assert "driver" in run["tool"]
    assert len(run["results"]) == 1
    assert run["results"][0]["ruleId"] == "ARCH-001"
    assert run["results"][0]["level"] == "error"


def test_junit_serializer():
    findings = _get_sample_findings()
    junit_str = JunitSerializer.serialize(findings)
    root = ET.fromstring(junit_str)
    assert root.tag == "testsuites"
    testsuite = root.find("testsuite")
    assert testsuite is not None
    assert testsuite.attrib["failures"] == "1"
    testcase = testsuite.find("testcase")
    assert testcase is not None
    failure = testcase.find("failure")
    assert failure is not None
    assert "Test Rule Violation" in failure.attrib["message"]


def test_policy_check_cli(tmp_path: Path):
    result_table = runner.invoke(app, ["policy", "check", "."])
    assert result_table.exit_code == 0
    assert (
        "Policy Evaluation Findings" in result_table.output
        or "Checked" in result_table.output
    )

    sarif_out = tmp_path / "report.sarif"
    result_sarif = runner.invoke(
        app, ["policy", "check", ".", "--format", "sarif", "--output", str(sarif_out)]
    )
    assert result_sarif.exit_code == 0
    assert sarif_out.exists()
    sarif_data = json.loads(sarif_out.read_text("utf-8"))
    assert sarif_data["version"] == "2.1.0"

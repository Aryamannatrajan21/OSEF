import xml.etree.ElementTree as ET
from typing import List
from osef.epe.core.result import Finding
from osef.epe.core.severity import Severity


class JunitSerializer:
    """Serializes EPE policy evaluation Findings to JUnit XML format."""

    @staticmethod
    def serialize(findings: List[Finding]) -> str:
        testsuites = ET.Element("testsuites", name="OSEF Policy Engine Evaluation")

        failures = sum(
            1
            for f in findings
            if f.severity in (Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM)
        )
        testsuite = ET.SubElement(
            testsuites,
            "testsuite",
            name="EPE Policies",
            tests=str(max(1, len(findings))),
            failures=str(failures),
            errors="0",
        )

        if not findings:
            ET.SubElement(
                testsuite, "testcase", classname="osef.epe", name="no_violations_found"
            )
        else:
            for finding in findings:
                testcase = ET.SubElement(
                    testsuite,
                    "testcase",
                    classname=f"osef.epe.{finding.category.value if hasattr(finding.category, 'value') else finding.category}",
                    name=f"[{finding.provenance.rule_id}] {finding.title}",
                )

                if finding.severity in (
                    Severity.CRITICAL,
                    Severity.HIGH,
                    Severity.MEDIUM,
                ):
                    failure_type = f"Severity.{finding.severity.value}"
                    failure_msg = f"{finding.title}: {finding.description}"
                    failure_el = ET.SubElement(
                        testcase, "failure", message=failure_msg, type=failure_type
                    )
                    failure_text = (
                        f"Rule ID: {finding.provenance.rule_id}\\n"
                        f"Severity: {finding.severity.value}\\n"
                        f"Evidence: {finding.evidence.description}\\n"
                        f"Affected Nodes: {', '.join(str(n) for n in finding.evidence.affected_nodes)}\\n"
                        f"Recommendation: {finding.recommendation.action}\\n"
                    )
                    failure_el.text = failure_text

        return ET.tostring(testsuites, encoding="unicode", xml_declaration=True)

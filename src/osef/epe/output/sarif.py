import json
from typing import Any, Dict, List
from osef.epe.core.result import Finding
from osef.epe.core.severity import Severity


class SarifSerializer:
    """Serializes EPE policy evaluation Findings to SARIF 2.1.0 format."""

    @staticmethod
    def serialize(findings: List[Finding]) -> str:
        return json.dumps(SarifSerializer.to_dict(findings), indent=2)

    @staticmethod
    def to_dict(findings: List[Finding]) -> Dict[str, Any]:
        rules_map: Dict[str, Dict[str, Any]] = {}
        results: List[Dict[str, Any]] = []

        for finding in findings:
            rule_id = finding.provenance.rule_id
            if rule_id not in rules_map:
                rules_map[rule_id] = {
                    "id": rule_id,
                    "name": finding.title,
                    "shortDescription": {"text": finding.title},
                    "fullDescription": {"text": finding.description},
                    "help": {
                        "text": f"Recommendation: {finding.recommendation.action}\\n\\n{finding.recommendation.description}"
                    },
                    "properties": {
                        "category": str(
                            finding.category.value
                            if hasattr(finding.category, "value")
                            else finding.category
                        ),
                        "precision": "high" if finding.confidence >= 0.8 else "medium",
                    },
                }

            level = "warning"
            if finding.severity in (Severity.CRITICAL, Severity.HIGH):
                level = "error"
            elif finding.severity == Severity.INFO:
                level = "note"

            locations: List[Dict[str, Any]] = []
            if finding.evidence.affected_nodes:
                for node in finding.evidence.affected_nodes:
                    locations.append(
                        {"physicalLocation": {"artifactLocation": {"uri": str(node)}}}
                    )
            elif finding.evidence.affected_edges:
                for edge in finding.evidence.affected_edges:
                    locations.append(
                        {"physicalLocation": {"artifactLocation": {"uri": str(edge)}}}
                    )
            else:
                locations.append(
                    {"physicalLocation": {"artifactLocation": {"uri": "."}}}
                )

            result_entry: Dict[str, Any] = {
                "ruleId": rule_id,
                "level": level,
                "message": {
                    "text": f"{finding.title}: {finding.description} | Evidence: {finding.evidence.description}"
                },
                "locations": locations,
                "properties": {
                    "confidence": finding.confidence,
                    "recommendation": finding.recommendation.action,
                    "autofix_available": finding.autofix.available,
                },
            }
            results.append(result_entry)

        sarif_doc: Dict[str, Any] = {
            "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
            "version": "2.1.0",
            "runs": [
                {
                    "tool": {
                        "driver": {
                            "name": "OSEF Policy Engine",
                            "informationUri": "https://github.com/Aryamannatrajan21/OSEF",
                            "version": "1.0.0",
                            "rules": list(rules_map.values()),
                        }
                    },
                    "results": results,
                }
            ],
        }
        return sarif_doc

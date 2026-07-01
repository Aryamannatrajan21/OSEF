from typing import List, Any
from osef.core.epe import Finding


class BaselineSecurityPolicies:
    name = "baseline_security"

    def evaluate(self, graph: Any) -> List[Finding]:
        findings = []
        for node in graph.get_nodes():
            if (
                node.type == "Security.Vulnerability"
                and node.metadata.get("severity") == "CRITICAL"
            ):
                findings.append(
                    Finding(
                        rule_id="SEC-001",
                        severity="CRITICAL",
                        message=f"Critical vulnerability detected: {node.name}",
                        node_id=node.id,
                    )
                )
        return findings


def get_all_policies() -> list:
    return [BaselineSecurityPolicies()]

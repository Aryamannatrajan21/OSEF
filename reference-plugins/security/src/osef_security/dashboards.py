from typing import Dict, Any


class SecurityExposureDashboard:
    name = "security_exposure"

    def generate(self, graph: Any) -> Dict[str, Any]:
        critical = 0
        high = 0
        for node in graph.get_nodes():
            if node.type == "Security.Vulnerability":
                severity = node.metadata.get("severity", "LOW")
                if severity == "CRITICAL":
                    critical += 1
                elif severity == "HIGH":
                    high += 1

        return {"vulnerabilities": {"CRITICAL": critical, "HIGH": high}}


def get_dashboards() -> list:
    return [SecurityExposureDashboard()]

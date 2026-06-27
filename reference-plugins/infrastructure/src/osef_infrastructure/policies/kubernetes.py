from typing import List, Dict, Any
from osef.core.ekg import KnowledgeGraph
from osef_infrastructure.ikm import IKM

def check_missing_health_checks(graph: KnowledgeGraph) -> List[Dict[str, Any]]:
    violations = []
    # Simplified check: logic would normally traverse the k8s deployment nodes to check for probes
    for node in graph.get_nodes():
        if node.type == IKM.CONTAINER and "k8s" in node.id:
            if not node.metadata.get("liveness_probe"):
                violations.append({
                    "policy": "MissingHealthChecks",
                    "severity": "ERROR",
                    "node_id": node.id,
                    "message": "Kubernetes container missing liveness probe."
                })
    return violations

def get_kubernetes_policies() -> List[Any]:
    return [check_missing_health_checks]

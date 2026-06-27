from typing import List, Dict, Any
from osef.core.ekg import KnowledgeGraph
from osef_infrastructure.ikm import IKM

def check_unbounded_resources(graph: KnowledgeGraph) -> List[Dict[str, Any]]:
    violations = []
    for node in graph.get_nodes():
        if node.type == IKM.CONTAINER and "k8s" in node.id:
            if not node.metadata.get("resource_limits"):
                violations.append({
                    "policy": "UnboundedResources",
                    "severity": "WARNING",
                    "node_id": node.id,
                    "message": "Container has unbounded resources (no limits defined)."
                })
    return violations

def get_resources_policies() -> List[Any]:
    return [check_unbounded_resources]

from typing import List, Dict, Any
from osef.core.ekg import KnowledgeGraph
from osef_infrastructure.ikm import IKM

def check_latest_image_tags(graph: KnowledgeGraph) -> List[Dict[str, Any]]:
    violations = []
    for node in graph.get_nodes():
        if node.type == IKM.IMAGE:
            base_image = node.metadata.get("base_image", "")
            if ":" not in base_image or base_image.endswith(":latest"):
                violations.append({
                    "policy": "LatestImageTags",
                    "severity": "WARNING",
                    "node_id": node.id,
                    "message": f"Image '{base_image}' uses the 'latest' tag or specifies no tag."
                })
        elif node.type == IKM.CONTAINER or node.type == IKM.SERVICE:
            image = node.metadata.get("image", "")
            if ":" not in image or image.endswith(":latest"):
                violations.append({
                    "policy": "LatestImageTags",
                    "severity": "WARNING",
                    "node_id": node.id,
                    "message": f"Service/Container uses 'latest' tag: '{image}'."
                })
    return violations

def get_container_policies() -> List[Any]:
    return [check_latest_image_tags]

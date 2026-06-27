from typing import Dict, Any
from osef.core.ekg import KnowledgeGraph
from osef_infrastructure.ikm import IKM

class Dashboard:
    name = "base"
    
    def generate(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        return {}

class InventoryDashboard(Dashboard):
    name = "inventory"
    
    def generate(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        inventory = {
            "services": 0,
            "containers": 0,
            "images": 0,
            "deployments": 0,
            "volumes": 0
        }
        for node in graph.get_nodes():
            if node.type == IKM.SERVICE:
                inventory["services"] += 1
            elif node.type == IKM.CONTAINER:
                inventory["containers"] += 1
            elif node.type == IKM.IMAGE:
                inventory["images"] += 1
            elif node.type == IKM.DEPLOYMENT:
                inventory["deployments"] += 1
            elif node.type == IKM.VOLUME:
                inventory["volumes"] += 1
                
        return inventory

class TopologyDashboard(Dashboard):
    name = "topology"
    def generate(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        return {"nodes": len(graph.get_nodes()), "edges": len(graph.get_edges())}

class SecurityDashboard(Dashboard):
    name = "security"
    def generate(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        return {"status": "Scaffolded"}

class ResourcesDashboard(Dashboard):
    name = "resources"
    def generate(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        return {"status": "Scaffolded"}

class ComplianceDashboard(Dashboard):
    name = "compliance"
    def generate(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        return {"status": "Scaffolded"}

def get_dashboards() -> list:
    return [
        InventoryDashboard(),
        TopologyDashboard(),
        SecurityDashboard(),
        ResourcesDashboard(),
        ComplianceDashboard()
    ]

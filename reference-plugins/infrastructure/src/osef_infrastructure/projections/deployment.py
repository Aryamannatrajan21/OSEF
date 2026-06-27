from typing import Any, Dict
from osef.core.ekg import KnowledgeGraph
from osef_infrastructure.ikm import IKM

class DeploymentTopologyProjection:
    """
    Projects the EKG into a Deployment Topology view.
    Designed to be compatible with osef_visualization.ir.ProjectedGraph dynamically.
    """
    
    name = "deployment_topology"
    description = "Shows services, containers, and deployment targets"
    
    def project(self, graph: KnowledgeGraph, **kwargs: Any) -> Any:
        # We optionally import ProjectedGraph so we don't hard crash if visualization is missing
        try:
            from osef_visualization.ir import ProjectedGraph
            ir = ProjectedGraph(name="Deployment Topology")
            
            for node in graph.get_nodes():
                if node.type in [IKM.SERVICE, IKM.CONTAINER, IKM.DEPLOYMENT]:
                    ir.add_node(node.id, node.name, node.type)
                    
            for edge in graph.get_edges():
                if edge.relation_type in [IKM.DEPLOYED_TO, IKM.MOUNTS, IKM.CONNECTS_TO, IKM.REQUIRES]:
                    ir.add_edge(edge.source_id, edge.target_id, edge.relation_type)
                    
            return ir
        except ImportError:
            raise RuntimeError("Visualization plugin required to run projections.")

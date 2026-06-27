from typing import Any
from osef.core.ekg import KnowledgeGraph, GraphDelta, Edge

class SoftwareToLayerRule:
    name = "software_belongs_to_layer"
    description = "Correlates Software.Package to Architecture.Layer"
    
    def evaluate(self, graph: KnowledgeGraph) -> GraphDelta:
        delta = GraphDelta()
        packages = [n for n in graph.get_nodes() if n.type == "Software.Package"]
        layers = [n for n in graph.get_nodes() if n.type == "Architecture.Layer"]
        
        for pkg in packages:
            for layer in layers:
                if layer.name in pkg.name:
                    delta.edges_to_add.append(Edge(
                        source_id=pkg.id,
                        target_id=layer.id,
                        relation_type="BELONGS_TO"
                    ))
        return delta

class InfrastructureToComponentRule:
    name = "infrastructure_implements_component"
    description = "Correlates Infrastructure.Service to Architecture.Component"
    
    def evaluate(self, graph: KnowledgeGraph) -> GraphDelta:
        return GraphDelta()

class DocumentationToComponentRule:
    name = "documentation_describes_component"
    description = "Correlates Documentation to Architecture.Component"
    
    def evaluate(self, graph: KnowledgeGraph) -> GraphDelta:
        return GraphDelta()

class SecurityToBoundaryRule:
    name = "security_protects_boundary"
    description = "Correlates Security.Control to Architecture.Boundary"
    
    def evaluate(self, graph: KnowledgeGraph) -> GraphDelta:
        return GraphDelta()

def get_correlation_rules() -> list:
    return [
        SoftwareToLayerRule(),
        InfrastructureToComponentRule(),
        DocumentationToComponentRule(),
        SecurityToBoundaryRule()
    ]

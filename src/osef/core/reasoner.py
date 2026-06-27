from pydantic import BaseModel, Field
from typing import List, Dict, Any
from osef.core.ekg import KnowledgeGraph, Node, Edge
from osef.core.graph_query import GraphQuery
from osef.sdk.registry.domain_registry import DomainRegistry
from osef.sdk.registry.correlation_registry import CorrelationRegistry

class ReasoningResult(BaseModel):
    """
    Immutable reasoning result produced by the EngineeringReasoner.
    """
    summary: str
    evidence: List[Any] = Field(default_factory=list)
    traversal_paths: List[List[Edge]] = Field(default_factory=list)
    related_nodes: List[Node] = Field(default_factory=list)
    confidence: float = 1.0
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ReasoningContext(BaseModel):
    """
    Immutable execution context for the EngineeringReasoner.
    """
    graph: KnowledgeGraph
    query: GraphQuery
    domain_registry: DomainRegistry
    correlation_registry: CorrelationRegistry
    execution_metadata: Dict[str, Any] = Field(default_factory=dict)
    
    class Config:
        arbitrary_types_allowed = True

class EngineeringReasoner:
    """
    Read-only intelligence layer. 
    Composes GraphQuery to answer higher-order engineering questions.
    Must never modify the graph.
    """
    
    def __init__(self, context: ReasoningContext):
        self.context = context
        self.query = context.query
        self.graph = context.graph

    def dependency_chain(self, node_id: str) -> ReasoningResult:
        """
        Traces all transitive dependencies (e.g., Software or Infrastructure).
        """
        start_node = self.query.get_node(node_id)
        if not start_node:
            return ReasoningResult(summary=f"Node {node_id} not found", confidence=0.0)
            
        # Example using the query API: trace DEPENDS_ON edges
        descendants = self.query.descendants(node_id) # Generic descendants
        
        return ReasoningResult(
            summary=f"Dependency chain for {start_node.name}",
            related_nodes=descendants,
            metadata={"depth": len(descendants)}
        )

    def deployment_chain(self, node_id: str) -> ReasoningResult:
        """
        Traces a software component down to its physical/logical deployment.
        """
        start_node = self.query.get_node(node_id)
        if not start_node:
            return ReasoningResult(summary="Node not found", confidence=0.0)
            
        path = self.query.trace(node_id, "DEPLOYED_AS")
        nodes = []
        if path:
            for edge in path:
                n = self.query.get_node(edge.source_id)
                if n:
                    nodes.append(n)
            last_n = self.query.get_node(path[-1].target_id)
            if last_n:
                nodes.append(last_n)
            
        return ReasoningResult(
            summary=f"Deployment chain for {start_node.name}",
            traversal_paths=[path],
            related_nodes=nodes
        )

    def architecture_chain(self, node_id: str) -> ReasoningResult:
        """
        Traces infrastructure/software up to its architectural boundary.
        """
        start_node = self.query.get_node(node_id)
        if not start_node:
            return ReasoningResult(summary="Node not found", confidence=0.0)
            
        path_belongs = self.query.trace(node_id, "BELONGS_TO")
        path_implements = self.query.trace(node_id, "IMPLEMENTS")
        
        path = path_belongs or path_implements
        nodes = []
        if path:
            for edge in path:
                target_node = self.query.get_node(edge.target_id)
                if target_node:
                    nodes.append(target_node)
            
        return ReasoningResult(
            summary=f"Architecture trace for {start_node.name}",
            traversal_paths=[path],
            related_nodes=nodes
        )

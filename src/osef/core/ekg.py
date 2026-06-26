"""
Engineering Knowledge Graph (EKG) core structures.
"""

from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field

from osef.contracts.exceptions import OSEFError


class EKGError(OSEFError):
    """Base exception for EKG errors."""

    pass


class Node(BaseModel):
    """A single artifact, document, or concept in the EKG."""

    id: str
    type: str
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, str] = Field(default_factory=dict)


class Edge(BaseModel):
    """A directed relationship between two nodes in the EKG."""

    source_id: str
    target_id: str
    relation_type: str
    metadata: Dict[str, str] = Field(default_factory=dict)


class KnowledgeGraph(BaseModel):
    """The Engineering Knowledge Graph structure."""

    version: str = "1.0.0"
    nodes: Dict[str, Node] = Field(default_factory=dict)
    edges: List[Edge] = Field(default_factory=list)

    def add_node(self, node: Node) -> None:
        if node.id in self.nodes:
            raise EKGError(f"Node '{node.id}' already exists.")
        self.nodes[node.id] = node

    def add_edge(self, edge: Edge) -> None:
        if edge.source_id not in self.nodes:
            raise EKGError(f"Source node '{edge.source_id}' does not exist.")
        if edge.target_id not in self.nodes:
            raise EKGError(f"Target node '{edge.target_id}' does not exist.")
        self.edges.append(edge)

    def validate_graph(self) -> bool:
        """Ensure all edges point to valid nodes."""
        for edge in self.edges:
            if edge.source_id not in self.nodes or edge.target_id not in self.nodes:
                return False
        return True

    def export_json(self) -> str:
        """Export the graph to a JSON string."""
        return self.model_dump_json(indent=2)

    def merge_delta(self, delta: "GraphDelta", provenance: Dict[str, str]) -> None:
        """
        Merge an immutable GraphDelta into the EKG.
        Records provenance on all added elements.
        """
        if delta.validation_state != "VALIDATED":
            raise EKGError("Cannot merge an unvalidated GraphDelta")

        for node in delta.nodes_to_add:
            if node.id in self.nodes:
                continue  # or raise error depending on merge strategy
            node.metadata["created_by"] = provenance.get("plugin", "unknown")
            node.metadata["execution_id"] = provenance.get("execution_id", "unknown")
            self.nodes[node.id] = node

        for edge in delta.edges_to_add:
            edge.metadata["created_by"] = provenance.get("plugin", "unknown")
            edge.metadata["execution_id"] = provenance.get("execution_id", "unknown")
            self.edges.append(edge)


class GraphDelta(BaseModel):
    """
    An immutable proposal of changes to the KnowledgeGraph.
    Returned by GraphEnrichmentCapabilities.
    """

    nodes_to_add: List[Node] = Field(default_factory=list)
    edges_to_add: List[Edge] = Field(default_factory=list)
    nodes_to_update: List[Node] = Field(default_factory=list)
    edges_to_update: List[Edge] = Field(default_factory=list)
    nodes_to_remove: List[str] = Field(default_factory=list)
    edges_to_remove: List[str] = Field(default_factory=list)
    diagnostics: List[Dict[str, str]] = Field(default_factory=list)
    metadata: Dict[str, str] = Field(default_factory=dict)
    validation_state: str = "PENDING"

    def validate_delta(self, current_graph: "KnowledgeGraph") -> bool:
        """Validate delta against current graph."""
        # Check dangling edges
        for edge in self.edges_to_add:
            if edge.source_id not in current_graph.nodes and edge.source_id not in [
                n.id for n in self.nodes_to_add
            ]:
                self.diagnostics.append(
                    {"error": f"Missing source node: {edge.source_id}"}
                )
                self.validation_state = "FAILED"
                return False
            if edge.target_id not in current_graph.nodes and edge.target_id not in [
                n.id for n in self.nodes_to_add
            ]:
                self.diagnostics.append(
                    {"error": f"Missing target node: {edge.target_id}"}
                )
                self.validation_state = "FAILED"
                return False

        self.validation_state = "VALIDATED"
        return True

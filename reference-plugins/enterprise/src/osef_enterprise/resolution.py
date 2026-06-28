"""
Ownership Resolution Engine.
"""

from typing import Optional, List
from osef.core.ekg import KnowledgeGraph, Node


class OwnershipResolutionEngine:
    """
    Resolves ownership for a given node across multiple sources:
    - CODEOWNERS
    - Service Catalog
    - Explicit Architecture mappings
    - Manual overrides
    """

    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph

    def resolve_owner(self, node_id: str) -> Optional[Node]:
        """
        Returns the Team or Member node that owns this node, if found.
        """
        # Look for explicit OWNED_BY edges in the graph
        for edge in self.graph.edges:
            if edge.source_id == node_id and edge.relation_type == "OWNED_BY":
                owner_node = self.graph.get_node(edge.target_id)
                if owner_node:
                    return owner_node
        return None

    def resolve_maintainers(self, node_id: str) -> List[Node]:
        """
        Returns all maintaining teams or members.
        """
        maintainers = []
        for edge in self.graph.edges:
            if edge.source_id == node_id and edge.relation_type == "MAINTAINS":
                owner_node = self.graph.get_node(edge.target_id)
                if owner_node:
                    maintainers.append(owner_node)
        return maintainers

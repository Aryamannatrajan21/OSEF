from typing import Dict, Any, List
from osef.core.ekg import KnowledgeGraph, Node, Edge


class RuleContext:
    """
    Wraps the Engineering Knowledge Graph to provide a semantic query API.
    Includes a Shared Graph Query Cache so multiple rules do not repeat expensive traversals.
    """
    def __init__(self, graph: KnowledgeGraph, policy_version: str):
        self.graph = graph
        self.policy_version = policy_version
        self._cache: Dict[str, Any] = {}

    def get_nodes_by_type(self, node_type: str) -> List[Node]:
        cache_key = f"nodes_by_type:{node_type}"
        if cache_key not in self._cache:
            self._cache[cache_key] = [n for n in self.graph.nodes.values() if n.type == node_type]
        return self._cache[cache_key]

    def get_nodes_by_semantic_role(self, role: str) -> List[Node]:
        cache_key = f"nodes_by_role:{role}"
        if cache_key not in self._cache:
            self._cache[cache_key] = [
                n for n in self.graph.nodes.values() 
                if n.metadata.get("semantic_role", "").lower() == role.lower()
            ]
        return self._cache[cache_key]

    def get_edges_by_type(self, relation_type: str) -> List[Edge]:
        cache_key = f"edges_by_type:{relation_type}"
        if cache_key not in self._cache:
            self._cache[cache_key] = [e for e in self.graph.edges if e.relation_type == relation_type]
        return self._cache[cache_key]

    def find_dependencies(self) -> List[Edge]:
        return self.get_edges_by_type("IMPORTS")

    def find_calls(self) -> List[Edge]:
        return self.get_edges_by_type("CALLS")

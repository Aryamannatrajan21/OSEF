from typing import List, Dict, Any, Optional
from osef.core.ekg import KnowledgeGraph, Node, Edge

class GraphQuery:
    """
    Stable Query Platform for OSEF. Lazily evaluated, heavily cached.
    """
    def __init__(self, graph: KnowledgeGraph) -> None:
        self.graph = graph
        self._cache: Dict[str, Any] = {}

    def get_nodes(self, type_filter: Optional[str] = None) -> List[Node]:
        cache_key = f"nodes:{type_filter}" if type_filter else "nodes:all"
        if cache_key not in self._cache:
            if type_filter:
                self._cache[cache_key] = [n for n in self.graph.nodes.values() if n.type == type_filter]
            else:
                self._cache[cache_key] = list(self.graph.nodes.values())
        return self._cache[cache_key]

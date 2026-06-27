from typing import List, Dict, Set, Optional
from osef.core.ekg import KnowledgeGraph, Node, Edge
from collections import deque


class GraphQuery:
    """
    Generic traversal API for the Engineering Knowledge Graph.
    Contains no engineering semantics.
    """

    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph
        # Index edges for fast traversal
        self._out_edges: Dict[str, List[Edge]] = {}
        self._in_edges: Dict[str, List[Edge]] = {}
        for edge in graph.edges:
            self._out_edges.setdefault(edge.source_id, []).append(edge)
            self._in_edges.setdefault(edge.target_id, []).append(edge)

    def get_node(self, node_id: str) -> Optional[Node]:
        return self.graph.nodes.get(node_id)

    def get_edge(self, source_id: str, target_id: str) -> Optional[Edge]:
        for edge in self._out_edges.get(source_id, []):
            if edge.target_id == target_id:
                return edge
        return None

    def neighbors(self, node_id: str) -> List[Node]:
        node_ids = set()
        for edge in self._out_edges.get(node_id, []):
            node_ids.add(edge.target_id)
        for edge in self._in_edges.get(node_id, []):
            node_ids.add(edge.source_id)
        return [self.graph.nodes[nid] for nid in node_ids if nid in self.graph.nodes]

    def successors(self, node_id: str) -> List[Node]:
        return [
            self.graph.nodes[edge.target_id]
            for edge in self._out_edges.get(node_id, [])
            if edge.target_id in self.graph.nodes
        ]

    def predecessors(self, node_id: str) -> List[Node]:
        return [
            self.graph.nodes[edge.source_id]
            for edge in self._in_edges.get(node_id, [])
            if edge.source_id in self.graph.nodes
        ]

    def find_path(self, source_id: str, target_id: str) -> List[Edge]:
        from typing import Any

        # Simple BFS
        queue: Any = deque([(source_id, [])])
        visited = {source_id}

        while queue:
            current, path = queue.popleft()
            if current == target_id:
                return path  # type: ignore

            for edge in self._out_edges.get(current, []):
                if edge.target_id not in visited:
                    visited.add(edge.target_id)
                    queue.append((edge.target_id, path + [edge]))
        return []

    def trace(self, start_id: str, edge_type: str) -> List[Edge]:
        path = []
        visited = set()
        current = start_id

        while current not in visited:
            visited.add(current)
            edges = [
                e
                for e in self._out_edges.get(current, [])
                if e.relation_type == edge_type
            ]
            if not edges:
                break
            # Just take the first matching edge for a simple linear trace
            edge = edges[0]
            path.append(edge)
            current = edge.target_id
        return path

    def reachable(self, node_id: str) -> Set[str]:
        return set(n.id for n in self.descendants(node_id))

    def ancestors(self, node_id: str) -> List[Node]:
        visited = set()
        queue = deque([node_id])
        while queue:
            curr = queue.popleft()
            for edge in self._in_edges.get(curr, []):
                if edge.source_id not in visited:
                    visited.add(edge.source_id)
                    queue.append(edge.source_id)
        return [self.graph.nodes[nid] for nid in visited if nid in self.graph.nodes]

    def descendants(self, node_id: str) -> List[Node]:
        visited = set()
        queue = deque([node_id])
        while queue:
            curr = queue.popleft()
            for edge in self._out_edges.get(curr, []):
                if edge.target_id not in visited:
                    visited.add(edge.target_id)
                    queue.append(edge.target_id)
        return [self.graph.nodes[nid] for nid in visited if nid in self.graph.nodes]

    def subgraph(self, node_ids: List[str]) -> List[Edge]:
        ids_set = set(node_ids)
        edges = []
        for n in ids_set:
            for edge in self._out_edges.get(n, []):
                if edge.target_id in ids_set:
                    edges.append(edge)
        return edges

    def layer(self, node_type: str) -> List[Node]:
        return [n for n in self.graph.nodes.values() if n.type == node_type]

    def connected_components(self) -> List[List[Node]]:
        # Mocked implementation for brevity
        return [list(self.graph.nodes.values())] if self.graph.nodes else []

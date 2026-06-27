from typing import List, Dict, Any, Optional, cast, Set
from collections import deque
from osef.core.ekg import KnowledgeGraph, Node, Edge


class GraphQuery:
    """
    Stable Query Platform for OSEF. Lazily evaluated, heavily cached.
    """

    def __init__(self, graph: KnowledgeGraph) -> None:
        self.graph = graph
        self._cache: Dict[str, Any] = {}

    def get_node(self, node_id: str) -> Optional[Node]:
        return self.graph.nodes.get(node_id)

    def get_nodes(self, type_filter: Optional[str] = None) -> List[Node]:
        cache_key = f"nodes:{type_filter}" if type_filter else "nodes:all"
        if cache_key not in self._cache:
            if type_filter:
                self._cache[cache_key] = [
                    n for n in self.graph.nodes.values() if n.type == type_filter
                ]
            else:
                self._cache[cache_key] = list(self.graph.nodes.values())
        return cast(List[Node], self._cache[cache_key])

    def get_edges(self) -> List[Edge]:
        return self.graph.edges

    def find_nodes_by_type(self, type_name: str) -> List[Node]:
        return self.get_nodes(type_filter=type_name)

    def find_edges_by_type(self, type_name: str) -> List[Edge]:
        cache_key = f"edges:{type_name}"
        if cache_key not in self._cache:
            self._cache[cache_key] = [
                e for e in self.graph.edges if e.relation_type == type_name
            ]
        return cast(List[Edge], self._cache[cache_key])

    def get_neighbors(
        self, node: Node, relation_type: Optional[str] = None, direction: str = "both"
    ) -> List[Node]:
        """
        Get neighboring nodes. direction can be 'in', 'out', or 'both'.
        """
        neighbors = []
        for edge in self.graph.edges:
            if relation_type and edge.relation_type != relation_type:
                continue

            if direction in ("out", "both") and edge.source_id == node.id:
                target_node = self.get_node(edge.target_id)
                if target_node:
                    neighbors.append(target_node)

            if direction in ("in", "both") and edge.target_id == node.id:
                source_node = self.get_node(edge.source_id)
                if source_node:
                    neighbors.append(source_node)

        return list({n.id: n for n in neighbors}.values())

    def find_path(self, start: Node, end: Node) -> Optional[List[Node]]:
        """
        Find shortest path between two nodes using BFS.
        """
        if start.id == end.id:
            return [start]

        queue = deque([(start, [start])])
        visited: Set[str] = {start.id}

        while queue:
            current_node, path = queue.popleft()

            for neighbor in self.get_neighbors(current_node, direction="out"):
                if neighbor.id == end.id:
                    return path + [neighbor]
                if neighbor.id not in visited:
                    visited.add(neighbor.id)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def subgraph(self, nodes: List[Node], edges: List[Edge]) -> "GraphQuery":
        """
        Return a new GraphQuery restricted to a subset of nodes and edges.
        """
        sub_kg = KnowledgeGraph()
        for n in nodes:
            sub_kg.add_node(n)
        for e in edges:
            sub_kg.add_edge(e)
        return GraphQuery(sub_kg)

    def layer(self, layer_name: str) -> "GraphQuery":
        """
        Return a subgraph where nodes/edges belong to a specific 'layer' in their metadata.
        """
        nodes = [
            n
            for n in self.graph.nodes.values()
            if n.metadata.get("layer") == layer_name
        ]
        node_ids = {n.id for n in nodes}
        edges = [
            e
            for e in self.graph.edges
            if e.source_id in node_ids and e.target_id in node_ids
        ]
        return self.subgraph(nodes, edges)

    def projection(self, projection_type: str) -> Any:
        """
        Entry point for projection plugins to generate an IR (ProjectedGraph).
        """
        raise NotImplementedError("Projections are generated via ProjectionRegistry.")

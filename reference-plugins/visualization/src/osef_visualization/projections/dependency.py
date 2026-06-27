from typing import Any
from osef.sdk.queries import GraphQuery
from osef_visualization.ir import (
    ProjectedGraph,
    ProjectionMetadata,
    ProjectedNode,
    ProjectedEdge,
)
from osef_visualization.projections.base import Projection
from osef_visualization.registries import ProjectionRegistry


class DependencyProjection(Projection):
    def get_name(self) -> str:
        return "dependency"

    def project(self, query: GraphQuery, **kwargs: Any) -> ProjectedGraph:
        metadata = ProjectionMetadata(
            name="Dependency View", version="1.0", statistics={}
        )

        nodes_dict = {}
        edges = []

        # Find dependency edges ('imports', 'depends_on')
        import_edges = query.find_edges_by_type("imports")
        depends_edges = query.find_edges_by_type("depends_on")
        all_dependency_edges = import_edges + depends_edges

        for edge in all_dependency_edges:
            edges.append(
                ProjectedEdge(
                    source_id=edge.source_id,
                    target_id=edge.target_id,
                    type=edge.relation_type,
                    label=edge.relation_type,
                    attributes={
                        "style": "dashed"
                        if edge.relation_type == "imports"
                        else "solid"
                    },
                )
            )

            # Ensure nodes are captured
            if edge.source_id not in nodes_dict:
                source_node = query.get_node(edge.source_id)
                if source_node:
                    nodes_dict[edge.source_id] = ProjectedNode(
                        id=source_node.id, type=source_node.type, label=source_node.name
                    )

            if edge.target_id not in nodes_dict:
                target_node = query.get_node(edge.target_id)
                if target_node:
                    nodes_dict[edge.target_id] = ProjectedNode(
                        id=target_node.id, type=target_node.type, label=target_node.name
                    )

        metadata.statistics = {"node_count": len(nodes_dict), "edge_count": len(edges)}

        return ProjectedGraph(
            metadata=metadata, nodes=list(nodes_dict.values()), edges=edges
        )


ProjectionRegistry.register("dependency", DependencyProjection)

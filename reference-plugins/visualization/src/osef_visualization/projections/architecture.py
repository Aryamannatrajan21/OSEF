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


class ArchitectureProjection(Projection):
    def get_name(self) -> str:
        return "architecture"

    def project(self, query: GraphQuery, **kwargs: Any) -> ProjectedGraph:
        metadata = ProjectionMetadata(
            name="Architecture View", version="1.0", statistics={}
        )
        nodes = []
        edges = []

        # Find architectural nodes
        packages = query.find_nodes_by_type("Package")
        modules = query.find_nodes_by_type("Module")

        for pkg in packages:
            nodes.append(
                ProjectedNode(
                    id=pkg.id,
                    type="Package",
                    label=pkg.name,
                    attributes={"shape": "folder"},
                )
            )

        for mod in modules:
            nodes.append(
                ProjectedNode(
                    id=mod.id,
                    type="Module",
                    label=mod.name,
                    attributes={"shape": "box"},
                )
            )

        # Find hierarchical edges ('contains')
        for edge in query.find_edges_by_type("contains"):
            edges.append(
                ProjectedEdge(
                    source_id=edge.source_id,
                    target_id=edge.target_id,
                    type="contains",
                    label="contains",
                )
            )

        metadata.statistics = {"node_count": len(nodes), "edge_count": len(edges)}

        return ProjectedGraph(metadata=metadata, nodes=nodes, edges=edges)


ProjectionRegistry.register("architecture", ArchitectureProjection)

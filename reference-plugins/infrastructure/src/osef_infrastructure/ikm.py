from osef.core.ekg import Node, Edge
from typing import Any


class IKM:
    """
    Infrastructure Knowledge Model (IKM) definitions.
    Provides canonical types for infrastructure nodes and edges.
    """

    # Node Types
    SERVICE = "Infrastructure.Service"
    CONTAINER = "Infrastructure.Container"
    IMAGE = "Infrastructure.Image"
    VOLUME = "Infrastructure.Volume"
    NETWORK = "Infrastructure.Network"
    SECRET = "Infrastructure.Secret"
    PORT = "Infrastructure.Port"
    DEPLOYMENT = "Infrastructure.Deployment"

    # Edge Types
    DEPLOYED_TO = "deployed_to"
    MOUNTS = "mounts"
    CONNECTS_TO = "connects_to"
    EXPOSES = "exposes"
    REQUIRES = "requires"
    USES_IMAGE = "uses_image"
    HAS_SECRET = "has_secret"

    @classmethod
    def create_node(
        cls,
        node_type: str,
        node_id: str,
        name: str,
        source_adapter: str,
        source_file: str,
        layer: str = "infrastructure",
        **metadata: Any,
    ) -> Node:
        """Helper to create namespaced infrastructure nodes with provenance."""
        meta = {
            "layer": layer,
            "source_adapter": source_adapter,
            "source_file": source_file,
            **metadata,
        }
        return Node(id=node_id, type=node_type, name=name, metadata=meta)

    @classmethod
    def create_edge(
        cls, source_id: str, target_id: str, relation_type: str, **metadata: Any
    ) -> Edge:
        """Helper to create infrastructure edges."""
        return Edge(
            source_id=source_id,
            target_id=target_id,
            relation_type=relation_type,
            metadata=metadata,
        )

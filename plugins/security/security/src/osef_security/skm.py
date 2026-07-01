from enum import Enum
from typing import Dict, Any
from osef.core.ekg import Node
import uuid


class SKM(str, Enum):
    """Security Knowledge Model Namespaced Types."""

    ASSET = "Security.Asset"
    BOUNDARY = "Security.Boundary"
    RISK = "Security.Risk"
    CONTROL = "Security.Control"
    FINDING = "Security.Finding"
    POLICY = "Security.Policy"
    VULNERABILITY = "Security.Vulnerability"
    EXPOSURE = "Security.Exposure"
    IDENTITY = "Security.Identity"
    SECRET = "Security.Secret"

    @classmethod
    def create_node(
        cls,
        type_name: str,
        name: str,
        source_adapter: str,
        metadata: Dict[str, Any] = None,
    ) -> Node:
        """
        Creates a SKM compliant node, enforcing provenance logic.
        """
        node_meta = metadata or {}
        # Enforce provenance tracking in the Security Domain
        node_meta["source_adapter"] = source_adapter

        return Node(
            id=f"{type_name}::{name}::{uuid.uuid4().hex[:8]}",
            type=type_name,
            name=name,
            metadata=node_meta,
            description=f"Security entity parsed by {source_adapter}",
        )

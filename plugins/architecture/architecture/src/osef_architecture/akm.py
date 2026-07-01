from enum import Enum
from typing import Dict, Any
from osef.core.ekg import Node
import uuid


class AKM(str, Enum):
    """Architecture Knowledge Model Namespaced Types."""

    DOMAIN = "Architecture.Domain"
    LAYER = "Architecture.Layer"
    COMPONENT = "Architecture.Component"
    BOUNDARY = "Architecture.Boundary"
    CONSTRAINT = "Architecture.Constraint"
    INTERFACE = "Architecture.Interface"
    DEPENDENCY = "Architecture.Dependency"
    DECISION = "Architecture.Decision"
    PATTERN = "Architecture.Pattern"
    VIEW = "Architecture.View"
    MODULE = "Architecture.Module"

    @classmethod
    def create_node(
        cls,
        type_name: str,
        name: str,
        source_adapter: str,
        metadata: Dict[str, Any] = None,
    ) -> Node:
        """
        Creates an AKM compliant node, enforcing provenance logic.
        """
        node_meta = metadata or {}
        # Enforce provenance tracking
        node_meta["source_adapter"] = source_adapter

        return Node(
            id=f"{type_name}::{name}::{uuid.uuid4().hex[:8]}",
            type=type_name,
            name=name,
            metadata=node_meta,
            description=f"Architecture entity parsed by {source_adapter}",
        )

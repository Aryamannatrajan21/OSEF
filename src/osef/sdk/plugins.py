"""
OSEF Plugin SDK.
"""

from typing import Protocol, runtime_checkable, Dict, Any, List, Optional
from pydantic import BaseModel, Field


class KnowledgeDomainManifest(BaseModel):
    """Manifest describing a Knowledge Domain."""

    name: str
    version: str
    node_types: List[str] = Field(default_factory=list)
    edge_types: List[str] = Field(default_factory=list)
    adapters: List[str] = Field(default_factory=list)
    projections: List[str] = Field(default_factory=list)
    dashboards: List[str] = Field(default_factory=list)
    policy_packs: List[str] = Field(default_factory=list)


class PluginManifest(BaseModel):
    """Manifest describing an OSEF Plugin."""

    name: str
    version: str
    description: str
    author: str
    dependencies: List[str] = Field(default_factory=list)
    knowledge_domain: Optional[KnowledgeDomainManifest] = None


@runtime_checkable
class PluginInterface(Protocol):
    """Protocol that all OSEF plugins must implement."""

    @property
    def manifest(self) -> PluginManifest:
        """Return the plugin's manifest."""
        ...

    async def initialize(self, context: Dict[str, Any]) -> None:
        """Initialize the plugin with the runtime context."""
        ...

    async def shutdown(self) -> None:
        """Cleanly shut down the plugin."""
        ...

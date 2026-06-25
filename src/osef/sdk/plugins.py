"""
OSEF Plugin SDK.
"""

from typing import Protocol, runtime_checkable, Dict, Any, List
from pydantic import BaseModel, Field


class PluginManifest(BaseModel):
    """Manifest describing an OSEF Plugin."""

    name: str
    version: str
    description: str
    author: str
    dependencies: List[str] = Field(default_factory=list)


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

from pathlib import Path
from typing import Dict, Any
from osef.core.ekg import KnowledgeGraph
from osef.sdk.events import EventBus
from osef.sdk.capabilities import CapabilityDescriptor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from osef.sdk.host.host import ExtensionHost
    from osef.sdk.providers import BaseProvider


class ExtensionContext:
    def __init__(
        self,
        plugin_id: str,
        workspace_dir: Path,
        graph: KnowledgeGraph,
        event_bus: EventBus,
        host: "ExtensionHost" = None,
    ) -> None:
        self.plugin_id = plugin_id
        self.workspace_dir = workspace_dir
        self.graph = graph
        self.event_bus = event_bus
        self.host = host
        self.storage_dir = workspace_dir / ".osef" / "plugins" / plugin_id
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.cache: Dict[str, Any] = {}
        self.state: Dict[str, Any] = {}

    def register_capability(self, capability: CapabilityDescriptor) -> None:
        """Register a runtime capability from this plugin."""
        if self.host and hasattr(self.host, "registry"):
            self.host.registry.register(capability, self.plugin_id)

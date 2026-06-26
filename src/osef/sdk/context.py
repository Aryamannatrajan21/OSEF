from pathlib import Path
from typing import Dict, Any
from osef.core.ekg import KnowledgeGraph
from osef.sdk.events import EventBus

class ExtensionContext:
    def __init__(
        self,
        plugin_id: str,
        workspace_dir: Path,
        graph: KnowledgeGraph,
        event_bus: EventBus
    ) -> None:
        self.plugin_id = plugin_id
        self.workspace_dir = workspace_dir
        self.graph = graph
        self.event_bus = event_bus
        self.storage_dir = workspace_dir / ".osef" / "plugins" / plugin_id
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.cache: Dict[str, Any] = {}

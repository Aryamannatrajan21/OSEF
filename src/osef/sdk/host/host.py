import logging
from typing import Dict, Type
from pathlib import Path

from osef.sdk.plugin import OsefPlugin
from osef.sdk.context import ExtensionContext
from osef.core.ekg import KnowledgeGraph
from osef.sdk.events import EventBus, EventType
from osef.sdk.version import SDK_VERSION

logger = logging.getLogger(__name__)

class ExtensionHost:
    def __init__(self, workspace_dir: Path, graph: KnowledgeGraph) -> None:
        self.workspace_dir = workspace_dir
        self.graph = graph
        self.event_bus = EventBus()
        self.plugins: Dict[str, OsefPlugin] = {}

    def load_plugin(self, plugin_class: Type[OsefPlugin]) -> None:
        plugin = plugin_class()
        manifest = plugin.manifest
        
        # Negotiate Capabilities
        if manifest.capabilities.supports_sdk.version != SDK_VERSION:
            logger.error(f"Plugin {manifest.id} requires SDK {manifest.capabilities.supports_sdk.version}, but host is {SDK_VERSION}.")
            raise RuntimeError(f"Incompatible SDK version for {manifest.id}")
            
        self.event_bus.publish(EventType.BeforePluginLoad, {"plugin_id": manifest.id})
        
        context = ExtensionContext(
            plugin_id=manifest.id,
            workspace_dir=self.workspace_dir,
            graph=self.graph,
            event_bus=self.event_bus
        )
        
        plugin.activate(context)
        self.plugins[manifest.id] = plugin
        
        self.event_bus.publish(EventType.AfterPluginLoad, {"plugin_id": manifest.id})
        logger.info(f"Loaded plugin: {manifest.name} v{manifest.version}")

    def unload_all(self) -> None:
        for plugin in self.plugins.values():
            plugin.deactivate()
        self.plugins.clear()

"""
Plugin Registry to load and manage external OSEF plugins.
"""

from typing import Dict
from osef.sdk.plugins import PluginInterface
from osef.contracts.exceptions import OSEFError


class PluginError(OSEFError):
    """Exception raised for plugin registration errors."""

    pass


class PluginRegistry:
    """Manages discovery, validation, and lifecycle of plugins."""

    def __init__(self) -> None:
        self._plugins: Dict[str, PluginInterface] = {}

    def register(self, plugin: PluginInterface) -> None:
        """Register a new plugin."""
        manifest = plugin.manifest
        if manifest.name in self._plugins:
            raise PluginError(f"Plugin '{manifest.name}' is already registered.")
        self._plugins[manifest.name] = plugin

    def get_plugin(self, name: str) -> PluginInterface:
        """Retrieve a registered plugin by name."""
        if name not in self._plugins:
            raise PluginError(f"Plugin '{name}' not found.")
        return self._plugins[name]

    def list_plugins(self) -> Dict[str, str]:
        """List all registered plugins and their versions."""
        return {name: plugin.manifest.version for name, plugin in self._plugins.items()}

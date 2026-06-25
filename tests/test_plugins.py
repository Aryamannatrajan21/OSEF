import pytest
from typing import Dict, Any
from osef.sdk.plugins import PluginManifest
from osef.core.plugin_registry import PluginRegistry, PluginError


class MockPlugin:
    @property
    def manifest(self) -> PluginManifest:
        return PluginManifest(
            name="mock-plugin",
            version="1.0.0",
            description="A mock plugin",
            author="Test",
        )

    async def initialize(self, context: Dict[str, Any]) -> None:
        pass

    async def shutdown(self) -> None:
        pass


def test_plugin_registry():
    registry = PluginRegistry()
    plugin = MockPlugin()

    registry.register(plugin)  # type: ignore

    listed = registry.list_plugins()
    assert "mock-plugin" in listed
    assert listed["mock-plugin"] == "1.0.0"

    retrieved = registry.get_plugin("mock-plugin")
    assert retrieved.manifest.name == "mock-plugin"


def test_plugin_registry_duplicate():
    registry = PluginRegistry()
    plugin = MockPlugin()

    registry.register(plugin)  # type: ignore

    with pytest.raises(PluginError):
        registry.register(plugin)  # type: ignore

import yaml
from pathlib import Path
from osef.sdk.plugin import OsefPlugin, PluginManifest
from osef.sdk.context import ExtensionContext

class PythonPlugin(OsefPlugin):
    """
    The official Python reference implementation.
    Validates the Strangler Migration Strategy by providing an SDK-compliant parser.
    """
    @property
    def manifest(self) -> PluginManifest:
        # Load from plugin.yaml
        yaml_path = Path(__file__).parent.parent.parent / "plugin.yaml"
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        return PluginManifest(**data)

    def activate(self, context: ExtensionContext) -> None:
        """
        Register parsers, enrichers, and policies into the provided ExtensionContext.
        """
        # We will subscribe to event hooks here once migrated.
        pass

    def deactivate(self) -> None:
        """Cleanup resources."""
        pass

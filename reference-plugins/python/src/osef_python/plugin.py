import yaml
from pathlib import Path
from osef.sdk.plugin import OsefPlugin, PluginManifest
from osef.sdk.context import ExtensionContext
from osef.sdk.capabilities import ParserCapability

from osef_python.python import PythonParser
from osef_python.symbol_table import SymbolTable

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
        def _parse(pipeline_context):
            sym = SymbolTable()
            parser = PythonParser(sym)
            for python_file in pipeline_context.manifest.python_files:
                abs_path = pipeline_context.workspace_dir / python_file
                parser.parse_file(str(abs_path))
            return sym

        parser_cap = ParserCapability(language="python", factory=_parse)
        context.register_capability(parser_cap)

    def deactivate(self) -> None:
        """Cleanup resources."""
        pass

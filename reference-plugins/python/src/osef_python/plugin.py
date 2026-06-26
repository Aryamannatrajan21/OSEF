import yaml
from pathlib import Path
from osef.sdk.plugin import OsefPlugin, PluginManifest
from osef.sdk.context import ExtensionContext
from osef.sdk.providers import BaseParserProvider
from osef.sdk.pipeline import PipelineContext
from osef_python.python import PythonParser
from osef_python.symbol_table import SymbolTable

class PythonParserProvider(BaseParserProvider):
    @property
    def name(self) -> str:
        return "python_parser"
        
    @property
    def version(self) -> str:
        return "1.0.0"
        
    @property
    def language(self) -> str:
        return "python"
        
    def parse(self, context: PipelineContext) -> SymbolTable:
        # A stateless execution: we create a new SymbolTable and parser per execution
        sym = SymbolTable()
        parser = PythonParser(sym)
        for python_file in context.manifest.python_files:
            abs_path = context.workspace_dir / python_file
            parser.parse_file(str(abs_path))
        return sym

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
        context.register_provider(PythonParserProvider())

    def deactivate(self) -> None:
        """Cleanup resources."""
        pass

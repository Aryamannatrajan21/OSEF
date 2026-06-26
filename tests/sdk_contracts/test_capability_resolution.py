import pytest
from osef.sdk.registry import CapabilityRegistry
from osef.sdk.providers import BaseParserProvider
from osef.sdk.pipeline import PipelineContext
from osef.parser.symbol_table import SymbolTable

class MockPythonParser(BaseParserProvider):
    @property
    def name(self) -> str: return "mock_python"
    @property
    def version(self) -> str: return "1.0.0"
    @property
    def language(self) -> str: return "python"
    
    def parse(self, context: PipelineContext) -> SymbolTable:
        return SymbolTable()

class MockJavaParser(BaseParserProvider):
    @property
    def name(self) -> str: return "mock_java"
    @property
    def version(self) -> str: return "1.0.0"
    @property
    def language(self) -> str: return "java"
    
    def parse(self, context: PipelineContext) -> SymbolTable:
        return SymbolTable()

def test_capability_registry_resolution():
    registry = CapabilityRegistry()
    
    # Register multiple parsers
    registry.register(MockPythonParser(), "plugin.mock.python")
    registry.register(MockJavaParser(), "plugin.mock.java")
    
    # Resolve python
    python_parser = registry.resolve_parser("python")
    assert python_parser is not None
    assert python_parser.name == "mock_python"
    
    # Resolve java
    java_parser = registry.resolve_parser("java")
    assert java_parser is not None
    assert java_parser.name == "mock_java"
    
    # Resolve unknown
    go_parser = registry.resolve_parser("go")
    assert go_parser is None

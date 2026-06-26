import pytest
from osef.sdk.registry import CapabilityRegistry
from osef.sdk.capabilities import ParserCapability
from osef.parser.symbol_table import SymbolTable

def dummy_factory(context):
    return SymbolTable()

def test_capability_registry_resolution():
    registry = CapabilityRegistry()
    
    # Register multiple parser capabilities
    registry.register(ParserCapability(language="python", factory=dummy_factory), "plugin.mock.python")
    registry.register(ParserCapability(language="java", factory=dummy_factory), "plugin.mock.java")
    
    # Resolve python
    python_cap = registry.resolve_parser("python")
    assert python_cap is not None
    assert python_cap.language == "python"
    
    # Resolve java
    java_cap = registry.resolve_parser("java")
    assert java_cap is not None
    assert java_cap.language == "java"
    
    # Resolve unknown
    go_cap = registry.resolve_parser("go")
    assert go_cap is None

from pathlib import Path

from osef_python.python import PythonParser as PluginPythonParser
from osef_python.symbol_table import SymbolTable as PluginSymbolTable
from osef.parser.symbol_table import SymbolTable as CoreSymbolTable
from osef.parser.python import PythonParser as CorePythonParser

def test_parser_parity():
    """
    Validates Stage 1 of the Strangler Migration Strategy.
    Ensures that the extracted Plugin parser generates an identical Symbol Table
    as the frozen Core parser.
    """
    # 1. Setup Core Parser
    core_sym = CoreSymbolTable()
    core_parser = CorePythonParser(core_sym)
    
    # 2. Setup Plugin Parser
    plugin_sym = PluginSymbolTable()
    plugin_parser = PluginPythonParser(plugin_sym)
    
    # 3. Parse a file
    target_file = Path(__file__).parent.parent.parent.parent / "src" / "osef" / "core" / "pipeline.py"
    
    core_parser.parse_file(str(target_file))
    plugin_parser.parse_file(str(target_file))
    
    # 4. Compare Outputs
    assert len(core_sym.symbols) == len(plugin_sym.symbols)
    
    for symbol_id, core_symbol in core_sym.symbols.items():
        assert symbol_id in plugin_sym.symbols
        plugin_symbol = plugin_sym.symbols[symbol_id]
        
        # Validate exact parity
        assert core_symbol.name == plugin_symbol.name
        assert core_symbol.type == plugin_symbol.type
        assert core_symbol.file_path == plugin_symbol.file_path
        assert core_symbol.children_ids == plugin_symbol.children_ids
        assert core_symbol.metadata == plugin_symbol.metadata

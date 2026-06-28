import os
import sys
import hashlib
sys.path.insert(0, os.path.abspath("reference-plugins/typescript"))
from osef.sdk.language.builder import NormalizedSymbolBuilder
from src.parser.tree_sitter_adapter import TreeSitterTypeScriptAdapter
from src.extractor.extractor import TypeScriptSymbolExtractor

def test_single_class_extraction():
    fixture_path = "language-fixtures/symbols/single_class/test.ts"
    
    # 1. Parse
    parser = TreeSitterTypeScriptAdapter()
    ast = parser.parse(fixture_path)
    
    with open(fixture_path, "rb") as f:
        source_hash = hashlib.sha256(f.read()).hexdigest()
        
    # 2. Extract
    builder = NormalizedSymbolBuilder(
        language="typescript",
        parser="tree-sitter",
        parser_version="0.21.0",
        sdk_version="0.1.0",
        plugin_version="0.1.0",
        graph_schema_version="1.0"
    )
    extractor = TypeScriptSymbolExtractor(builder, fixture_path, source_hash)
    symbols = extractor.extract(ast)
    
    # 3. Assert
    assert len(symbols) == 1
    assert symbols[0].kind == "class"
    assert symbols[0].name == "UserService"
    assert symbols[0].parsing_provenance.ast_node_kind == "class_declaration"
    assert symbols[0].parsing_provenance.source_file == fixture_path
    
    print(f"Successfully extracted: {symbols[0].name} ({symbols[0].symbol_id})")

if __name__ == "__main__":
    test_single_class_extraction()

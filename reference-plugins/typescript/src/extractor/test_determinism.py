import os
import sys
import hashlib
sys.path.insert(0, os.path.abspath("reference-plugins/typescript"))
from src.osef.sdk.language.builder import NormalizedSymbolBuilder
from src.parser.tree_sitter_adapter import TreeSitterTypeScriptAdapter
from src.extractor.extractor import TypeScriptSymbolExtractor

def test_100x_determinism():
    fixture_path = "language-fixtures/symbols/single_class/test.ts"
    
    with open(fixture_path, "rb") as f:
        source_hash = hashlib.sha256(f.read()).hexdigest()
        
    parser = TreeSitterTypeScriptAdapter()
    ast = parser.parse(fixture_path)
    
    builder = NormalizedSymbolBuilder(
        language="typescript",
        parser="tree-sitter",
        parser_version="0.21.0",
        sdk_version="0.1.0",
        plugin_version="0.1.0",
        graph_schema_version="1.0"
    )
    
    # Run 100 times and hash the resulting Pydantic JSON dump
    hashes = set()
    for _ in range(100):
        extractor = TypeScriptSymbolExtractor(builder, fixture_path, source_hash)
        symbols = extractor.extract(ast)
        # Sort symbols for absolute safety
        symbols = sorted(symbols, key=lambda s: s.symbol_id)
        
        run_output = "[" + ",".join([s.model_dump_json() for s in symbols]) + "]"
        hashes.add(hashlib.sha256(run_output.encode("utf-8")).hexdigest())

    assert len(hashes) == 1
    print(f"✅ 100x Determinism Certification Passed! Hash: {list(hashes)[0]}")

if __name__ == "__main__":
    test_100x_determinism()

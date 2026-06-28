import os
import sys
sys.path.insert(0, os.path.abspath("reference-plugins/typescript"))
from src.osef.sdk.language.symbols import (
    NormalizedSymbol, NormalizedClass, NormalizedNamespace, ParsingProvenance, SemanticProvenance
)
from src.resolver.resolver import TypeScriptResolver

def test_resolver_passes():
    # 1. Mock symbols
    parsing_prov = ParsingProvenance(
        language="typescript",
        parser="tree-sitter",
        parser_version="0.21.0",
        source_file="test.ts",
        source_hash="abcd",
        ast_node_kind="class_declaration",
        source_range=[1,1,2,2]
    )
    semantic_prov = SemanticProvenance(
        semantic_stage="symbol_extraction",
        resolver_version="N/A",
        plugin_version="0.1",
        sdk_version="0.1",
        graph_schema_version="1.0",
        normalized_symbol_id="test_id"
    )
    
    ns_symbol = NormalizedNamespace(
        symbol_id="typescript::test.ts::MyNamespace::namespace",
        name="MyNamespace",
        parsing_provenance=parsing_prov,
        semantic_provenance=semantic_prov
    )
    
    class_symbol = NormalizedClass(
        symbol_id="typescript::test.ts::MyNamespace.UserService::class",
        name="MyNamespace.UserService",
        parsing_provenance=parsing_prov,
        semantic_provenance=semantic_prov,
        payload={"extends": "BaseService"}
    )
    
    base_class_symbol = NormalizedClass(
        symbol_id="typescript::test.ts::BaseService::class",
        name="BaseService",
        parsing_provenance=parsing_prov,
        semantic_provenance=semantic_prov
    )
    
    symbols = [ns_symbol, class_symbol, base_class_symbol]
    
    # 2. Resolve
    resolver = TypeScriptResolver()
    graph = resolver.resolve(symbols)
    
    # 3. Assert
    assert len(graph.nodes) == 3
    assert len(graph.edges) == 2
    
    declares_edge = [e for e in graph.edges if e.relationship_type == "DECLARES"][0]
    extends_edge = [e for e in graph.edges if e.relationship_type == "EXTENDS"][0]
    
    assert declares_edge.source_symbol_id == ns_symbol.symbol_id
    assert declares_edge.target_symbol_id == class_symbol.symbol_id
    
    assert extends_edge.source_symbol_id == class_symbol.symbol_id
    assert extends_edge.target_symbol_id == base_class_symbol.symbol_id
    
    print("✅ Resolver passes correctly generated language relationships without EKG leakages!")

if __name__ == "__main__":
    test_resolver_passes()

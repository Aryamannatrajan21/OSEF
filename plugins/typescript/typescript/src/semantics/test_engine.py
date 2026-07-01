import os
import sys

sys.path.insert(0, os.path.abspath("reference-plugins/typescript"))
from osef.sdk.language.resolver import ResolvedSymbolGraph, ResolvedRelationship
from osef.sdk.language.symbols import (
    NormalizedClass,
    ParsingProvenance,
    SemanticProvenance,
)
from src.semantics.engine import TypeScriptSemanticEngine


def test_semantic_engine():
    parsing_prov = ParsingProvenance(
        language="typescript",
        parser="tree-sitter",
        parser_version="0.21.0",
        source_file="test.ts",
        source_hash="abcd",
        ast_node_kind="class_declaration",
        source_range=[1, 1, 2, 2],
    )
    semantic_prov = SemanticProvenance(
        semantic_stage="symbol_extraction",
        resolver_version="N/A",
        plugin_version="0.1",
        sdk_version="0.1",
        graph_schema_version="1.0",
        normalized_symbol_id="test_id",
    )
    class_symbol = NormalizedClass(
        symbol_id="typescript::test.ts::UserService::class",
        name="UserService",
        parsing_provenance=parsing_prov,
        semantic_provenance=semantic_prov,
        modifiers=["public"],
    )

    graph = ResolvedSymbolGraph(
        nodes={class_symbol.symbol_id: class_symbol},
        edges=[
            ResolvedRelationship(
                relationship_id="rel1",
                source_symbol_id=class_symbol.symbol_id,
                target_symbol_id="typescript::test.ts::BaseService::class",
                relationship_type="EXTENDS",
            )
        ],
    )

    engine = TypeScriptSemanticEngine()
    facts = engine.analyze(graph)

    assert len(facts) == 2
    fact_types = [f.fact_type for f in facts]
    assert "INHERITS" in fact_types
    assert "IS_PUBLIC" in fact_types
    print("✅ Semantic Engine generated pure SemanticFacts without Graph schemas!")


if __name__ == "__main__":
    test_semantic_engine()

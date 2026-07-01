import os
import sys

sys.path.insert(0, os.path.abspath("reference-plugins/typescript"))
from osef.sdk.language.facts import SemanticFact
from src.projections.mapper import GraphMapper


def test_graph_mapper():
    facts = [
        SemanticFact(
            subject_symbol_id="typescript::test.ts::UserService::class",
            fact_type="INHERITS",
            attributes={"parent_id": "typescript::test.ts::BaseService::class"},
        ),
        SemanticFact(
            subject_symbol_id="typescript::test.ts::UserService::class",
            fact_type="IS_PUBLIC",
            attributes={},
        ),
    ]

    mapper = GraphMapper()
    delta = mapper.map_to_graph(facts)

    assert len(delta.nodes) == 1
    assert delta.nodes[0].node_id == "typescript::test.ts::UserService::class"
    assert delta.nodes[0].properties.get("is_public") is True

    assert len(delta.edges) == 1
    assert delta.edges[0].source_id == "typescript::test.ts::UserService::class"
    assert delta.edges[0].target_id == "typescript::test.ts::BaseService::class"
    assert delta.edges[0].relationship == "INHERITS"

    print(
        "✅ Graph Mapper correctly and deterministically translated SemanticFacts to a pure GraphDelta!"
    )


if __name__ == "__main__":
    test_graph_mapper()

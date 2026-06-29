from typing import Sequence, List
from pydantic import BaseModel, Field
from osef.sdk.language.facts import SemanticFact


# Basic Graph schema objects
class GraphNode(BaseModel):
    node_id: str
    labels: List[str]
    properties: dict = Field(default_factory=dict)


class GraphEdge(BaseModel):
    edge_id: str
    source_id: str
    target_id: str
    relationship: str
    properties: dict = Field(default_factory=dict)


class GraphDelta(BaseModel):
    nodes: List[GraphNode] = Field(default_factory=list)
    edges: List[GraphEdge] = Field(default_factory=list)


class GraphMapper:
    """
    Intentionally 'dumb' deterministic translation from SemanticFacts to GraphDelta.
    Does no reasoning, evaluation, or parsing.
    """

    def map_to_graph(self, facts: Sequence[SemanticFact]) -> GraphDelta:
        delta = GraphDelta()

        created_nodes = set()

        for fact in facts:
            # Emit a node for the subject
            if fact.subject_symbol_id not in created_nodes:
                delta.nodes.append(
                    GraphNode(
                        node_id=fact.subject_symbol_id,
                        labels=["Symbol"],
                        properties={"schema_version": fact.schema_version},
                    )
                )
                created_nodes.add(fact.subject_symbol_id)

            if fact.fact_type == "INHERITS":
                parent_id = fact.attributes.get("parent_id")
                delta.edges.append(
                    GraphEdge(
                        edge_id=f"{fact.subject_symbol_id}_INHERITS_{parent_id}",
                        source_id=fact.subject_symbol_id,
                        target_id=parent_id,
                        relationship="INHERITS",
                    )
                )
            elif fact.fact_type == "DEPENDS_ON":
                target_id = fact.attributes.get("target_id")
                delta.edges.append(
                    GraphEdge(
                        edge_id=f"{fact.subject_symbol_id}_DEPENDS_ON_{target_id}",
                        source_id=fact.subject_symbol_id,
                        target_id=target_id,
                        relationship="DEPENDS_ON",
                    )
                )
            elif fact.fact_type == "HAS_TYPE":
                type_id = fact.attributes.get("type_id")
                delta.edges.append(
                    GraphEdge(
                        edge_id=f"{fact.subject_symbol_id}_HAS_TYPE_{type_id}",
                        source_id=fact.subject_symbol_id,
                        target_id=type_id,
                        relationship="HAS_TYPE",
                    )
                )
            elif fact.fact_type == "IS_PUBLIC":
                # It's a property on the node
                for n in delta.nodes:
                    if n.node_id == fact.subject_symbol_id:
                        n.properties["is_public"] = True
            elif fact.fact_type == "OWNS":
                child_id = fact.attributes.get("child_id")
                delta.edges.append(
                    GraphEdge(
                        edge_id=f"{fact.subject_symbol_id}_OWNS_{child_id}",
                        source_id=fact.subject_symbol_id,
                        target_id=child_id,
                        relationship="OWNS",
                    )
                )
            elif fact.fact_type == "EXECUTES":
                target_id = fact.attributes.get("target_id")
                delta.edges.append(
                    GraphEdge(
                        edge_id=f"{fact.subject_symbol_id}_EXECUTES_{target_id}",
                        source_id=fact.subject_symbol_id,
                        target_id=target_id,
                        relationship="EXECUTES",
                    )
                )

        return delta

from typing import Sequence, List
from osef.sdk.language.resolver import ResolvedSymbolGraph
from osef.sdk.language.facts import SemanticFact


class StructuralAnalyzer:
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]):
        for edge in graph.edges:
            if edge.relationship_type == "EXTENDS":
                facts.append(
                    SemanticFact(
                        subject_symbol_id=edge.source_symbol_id,
                        fact_type="INHERITS",
                        attributes={"parent_id": edge.target_symbol_id},
                    )
                )


class DependencyAnalyzer:
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]):
        for edge in graph.edges:
            if edge.relationship_type == "IMPORTS":
                facts.append(
                    SemanticFact(
                        subject_symbol_id=edge.source_symbol_id,
                        fact_type="DEPENDS_ON",
                        attributes={"target_id": edge.target_symbol_id},
                    )
                )


class TypeAnalyzer:
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]):
        for edge in graph.edges:
            if edge.relationship_type == "USES_TYPE":
                facts.append(
                    SemanticFact(
                        subject_symbol_id=edge.source_symbol_id,
                        fact_type="HAS_TYPE",
                        attributes={"type_id": edge.target_symbol_id},
                    )
                )


class VisibilityAnalyzer:
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]):
        for node in graph.nodes.values():
            if "public" in node.modifiers:
                facts.append(
                    SemanticFact(
                        subject_symbol_id=node.symbol_id,
                        fact_type="IS_PUBLIC",
                        attributes={},
                    )
                )


class OwnershipAnalyzer:
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]):
        for edge in graph.edges:
            if edge.relationship_type == "DECLARES":
                facts.append(
                    SemanticFact(
                        subject_symbol_id=edge.source_symbol_id,
                        fact_type="OWNS",
                        attributes={"child_id": edge.target_symbol_id},
                    )
                )


class ExecutionAnalyzer:
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]):
        for edge in graph.edges:
            if edge.relationship_type == "CALLS":
                facts.append(
                    SemanticFact(
                        subject_symbol_id=edge.source_symbol_id,
                        fact_type="EXECUTES",
                        attributes={"target_id": edge.target_symbol_id},
                    )
                )


class TypeScriptSemanticEngine:
    """
    Transforms a ResolvedSymbolGraph into language-neutral engineering knowledge.
    Output remains exclusively SemanticFact objects.
    """

    def __init__(self):
        self.analyzers = [
            StructuralAnalyzer(),
            DependencyAnalyzer(),
            TypeAnalyzer(),
            VisibilityAnalyzer(),
            OwnershipAnalyzer(),
            ExecutionAnalyzer(),
        ]

    def analyze(self, graph: ResolvedSymbolGraph) -> Sequence[SemanticFact]:
        facts: List[SemanticFact] = []
        for analyzer in self.analyzers:
            analyzer.analyze(graph, facts)
        return facts

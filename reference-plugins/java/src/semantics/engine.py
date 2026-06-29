from typing import Sequence, List
from osef.sdk.language.resolver import ResolvedSymbolGraph
from osef.sdk.language.facts import SemanticFact


class AnalyzerProtocol:
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]) -> None:
        pass


class StructuralAnalyzer(AnalyzerProtocol):
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]) -> None:
        for edge in graph.edges:
            if edge.relationship_type == "EXTENDS":
                facts.append(
                    SemanticFact(
                        subject_symbol_id=edge.source_symbol_id,
                        fact_type="INHERITS",
                        attributes={"parent_id": edge.target_symbol_id},
                    )
                )


class DependencyAnalyzer(AnalyzerProtocol):
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]) -> None:
        for edge in graph.edges:
            if edge.relationship_type == "IMPORTS":
                facts.append(
                    SemanticFact(
                        subject_symbol_id=edge.source_symbol_id,
                        fact_type="DEPENDS_ON",
                        attributes={"target_id": edge.target_symbol_id},
                    )
                )


class VisibilityAnalyzer(AnalyzerProtocol):
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]) -> None:
        for node in graph.nodes.values():
            if "public" in node.modifiers:
                facts.append(
                    SemanticFact(
                        subject_symbol_id=node.symbol_id,
                        fact_type="IS_PUBLIC",
                        attributes={},
                    )
                )


class OwnershipAnalyzer(AnalyzerProtocol):
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]) -> None:
        for edge in graph.edges:
            if edge.relationship_type == "DECLARES":
                facts.append(
                    SemanticFact(
                        subject_symbol_id=edge.source_symbol_id,
                        fact_type="OWNS",
                        attributes={"child_id": edge.target_symbol_id},
                    )
                )


class ExecutionAnalyzer(AnalyzerProtocol):
    def analyze(self, graph: ResolvedSymbolGraph, facts: List[SemanticFact]) -> None:
        for edge in graph.edges:
            if edge.relationship_type == "CALLS":
                facts.append(
                    SemanticFact(
                        subject_symbol_id=edge.source_symbol_id,
                        fact_type="EXECUTES",
                        attributes={"target_id": edge.target_symbol_id},
                    )
                )


class JavaSemanticEngine:
    """
    Transforms a ResolvedSymbolGraph into language-neutral engineering knowledge.
    Output remains exclusively SemanticFact objects.
    """

    def __init__(self):
        self.analyzers = [
            StructuralAnalyzer(),
            DependencyAnalyzer(),
            VisibilityAnalyzer(),
            OwnershipAnalyzer(),
            ExecutionAnalyzer(),
        ]

    def analyze(self, graph: ResolvedSymbolGraph) -> Sequence[SemanticFact]:
        facts: List[SemanticFact] = []
        for analyzer in self.analyzers:
            analyzer.analyze(graph, facts)
        return facts

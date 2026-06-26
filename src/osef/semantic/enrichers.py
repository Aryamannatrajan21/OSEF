"""
Semantic Enrichment Orchestrator.
"""

from osef.parser.symbol_table import SymbolTable
from osef.semantic.classifier import SemanticClassifier
from osef.semantic.relationships import RelationshipEnricher


class SemanticEnricher:
    """
    Applies multiple heuristic passes to the SymbolTable to enrich nodes
    with semantic intent, documentation intelligence, and call graph data.
    """

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table
        self.classifier = SemanticClassifier(symbol_table)
        self.relationships = RelationshipEnricher(symbol_table)

    def enrich(self) -> None:
        """
        Run all semantic passes in order.
        """
        self.classifier.classify_all()
        self.relationships.enrich_calls()

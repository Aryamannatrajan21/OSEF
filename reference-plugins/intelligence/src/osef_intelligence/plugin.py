from osef_intelligence.debt import calculate_technical_debt
from osef_intelligence.health import calculate_repository_health
from typing import Any, Dict
from osef.core.ekg import KnowledgeGraph


class IntelligenceAnalyzer:
    """
    Entrypoint for the OSEF Intelligence plugin.
    Provides tools to analyze Technical Debt and Repository Health.
    """

    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph

    def get_technical_debt(self) -> Dict[str, Any]:
        return calculate_technical_debt(self.graph)

    def get_repository_health(self) -> Dict[str, Any]:
        return calculate_repository_health(self.graph)

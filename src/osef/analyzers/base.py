"""
Analyzer Interface.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any

from osef.core.ekg import KnowledgeGraph


class BaseAnalyzer(ABC):
    """
    All Engineering Analyzers must implement this interface.
    Analyzers ONLY consume the Engineering Knowledge Graph.
    """
    @abstractmethod
    def analyze(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        """
        Analyze the graph and return factual findings.
        """
        pass

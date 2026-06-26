"""
Analyzer Interface.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List

from osef.core.ekg import KnowledgeGraph
from osef.epe.core.result import Finding


class BaseAnalyzer(ABC):
    """
    Analyzers act as orchestrators. They consume the Knowledge Graph and the Findings
    produced by the Policy Engine to return structured facts.
    """

    def __init__(self, graph: KnowledgeGraph, findings: List[Finding]):
        self.graph = graph
        self.findings = findings

    @abstractmethod
    def analyze(self) -> Dict[str, Any]:
        """
        Produce factual findings and summarize rule violations.
        """
        pass

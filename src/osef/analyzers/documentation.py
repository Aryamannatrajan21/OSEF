"""
Documentation Analyzer.
"""

from typing import Dict, Any
from osef.analyzers.base import BaseAnalyzer


class DocumentationAnalyzer(BaseAnalyzer):
    """
    Extracts documentation facts from the Engineering Knowledge Graph.
    """

    def analyze(self) -> Dict[str, Any]:
        findings = {
            "total_elements": 0,
            "documented_elements": 0,
            "undocumented_elements": 0,
            "coverage_percentage": 0.0,
        }

        for node in self.graph.nodes.values():
            if node.type in ("module", "class", "method", "function"):
                findings["total_elements"] += 1
                if node.description:
                    findings["documented_elements"] += 1
                else:
                    findings["undocumented_elements"] += 1

        if findings["total_elements"] > 0:
            total: int = findings["total_elements"]  # type: ignore[assignment]
            docd: int = findings["documented_elements"]  # type: ignore[assignment]
            findings["coverage_percentage"] = (docd / total) * 100

        return findings

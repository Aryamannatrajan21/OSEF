"""
Architecture Analyzer.
"""
from typing import Dict, Any
from osef.core.ekg import KnowledgeGraph
from osef.analyzers.base import BaseAnalyzer


class ArchitectureAnalyzer(BaseAnalyzer):
    """
    Extracts architectural facts from the Engineering Knowledge Graph.
    """
    def analyze(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        findings = {
            "services": 0,
            "controllers": 0,
            "repositories": 0,
            "dtos": 0,
            "exceptions": 0,
            "total_components": 0
        }
        
        for node in graph.nodes.values():
            if node.type == "class":
                findings["total_components"] += 1
                role = node.metadata.get("semantic_role", "").lower()
                if role == "service":
                    findings["services"] += 1
                elif role == "controller":
                    findings["controllers"] += 1
                elif role == "repository":
                    findings["repositories"] += 1
                elif role == "dto":
                    findings["dtos"] += 1
                elif role == "exception":
                    findings["exceptions"] += 1
                    
        return findings

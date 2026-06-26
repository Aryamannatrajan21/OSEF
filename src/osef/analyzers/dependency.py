"""
Dependency Analyzer.
"""
from typing import Dict, Any
from osef.core.ekg import KnowledgeGraph
from osef.analyzers.base import BaseAnalyzer


class DependencyAnalyzer(BaseAnalyzer):
    """
    Extracts dependency facts from the Engineering Knowledge Graph.
    """
    def analyze(self) -> Dict[str, Any]:
        findings = {
            "total_imports": 0,
            "resolved_imports": 0,
            "broken_imports": 0,
            "external_dependencies": set()
        }
        
        for node in self.graph.nodes.values():
            if node.type == "import":
                findings["total_imports"] += 1
                if node.metadata.get("resolved") == "true":
                    findings["resolved_imports"] += 1
                else:
                    findings["broken_imports"] += 1
                    module_name = node.metadata.get("module") or node.name
                    if module_name:
                        root_module = module_name.split(".")[0]
                        findings["external_dependencies"].add(root_module)  # type: ignore[attr-defined]
                        
        # Convert set to list for JSON serialization
        findings["external_dependencies"] = list(findings["external_dependencies"])  # type: ignore[arg-type]
        return findings

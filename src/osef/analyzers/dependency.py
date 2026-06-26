"""
Dependency Analyzer.
"""

from typing import Dict, Any
from osef.analyzers.base import BaseAnalyzer


class DependencyAnalyzer(BaseAnalyzer):
    """
    Extracts dependency facts from the Engineering Knowledge Graph.
    """

    def analyze(self) -> Dict[str, Any]:
        total_imports = 0
        resolved_imports = 0
        broken_imports = 0
        external_dependencies: set[str] = set()

        for node in self.graph.nodes.values():
            if node.type == "import":
                total_imports += 1
                if node.metadata.get("resolved") == "true":
                    resolved_imports += 1
                else:
                    broken_imports += 1
                    module_name = node.metadata.get("module") or node.name
                    if isinstance(module_name, str):
                        root_module = module_name.split(".")[0]
                        external_dependencies.add(root_module)

        return {
            "total_imports": total_imports,
            "resolved_imports": resolved_imports,
            "broken_imports": broken_imports,
            "external_dependencies": list(external_dependencies),
        }

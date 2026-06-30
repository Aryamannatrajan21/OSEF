"""
Dependency Analyzer.
"""

from typing import Dict, Any
from osef.analyzers.base import BaseAnalyzer

import sys


class DependencyAnalyzer(BaseAnalyzer):
    """
    Extracts dependency facts from the Engineering Knowledge Graph.
    """

    def analyze(self) -> Dict[str, Any]:
        total_imports = 0
        resolved_imports = 0
        broken_imports = 0
        external_dependencies: set[str] = set()

        # Get standard library names (Python 3.10+)
        stdlib = (
            sys.stdlib_module_names if hasattr(sys, "stdlib_module_names") else set()
        )

        for node in self.graph.nodes.values():
            if node.type == "import":
                total_imports += 1
                if node.metadata.get("resolved") == "true":
                    resolved_imports += 1
                else:
                    module_name = node.metadata.get("module") or node.name
                    if isinstance(module_name, str):
                        root_module = module_name.split(".")[0]
                        if root_module in stdlib:
                            # It's a standard library import, consider it resolved/external
                            resolved_imports += 1
                        else:
                            # It's not standard library, and not resolved locally
                            broken_imports += 1
                            external_dependencies.add(root_module)
                    else:
                        broken_imports += 1

        return {
            "total_imports": total_imports,
            "resolved_imports": resolved_imports,
            "broken_imports": broken_imports,
            "external_dependencies": list(external_dependencies),
        }

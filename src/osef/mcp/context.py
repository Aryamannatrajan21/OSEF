"""
Context injection layer for the Model Context Protocol server.
Bridges EKG queries, architectural assessments, and policy findings.
"""

from typing import Dict, List, Any, Optional
from osef.core.pipeline import PipelineEngine
from osef.core.graph_query import GraphQuery
from osef.epe.setup import get_default_engine
from osef.intelligence.layer import IntelligenceLayer


class EKGContextService:
    """Provides high-level context queries against the Engineering Knowledge Graph."""

    def __init__(self, path: str = ".") -> None:
        self.path = path
        self.graph: Optional[Any] = None
        self.query: Optional[GraphQuery] = None
        self.findings: List[Any] = []
        self.assessment: Optional[Any] = None

    def _ensure_loaded(self) -> None:
        if self.graph is not None:
            return
        builder = PipelineEngine(self.path)
        self.graph = builder.build()
        self.query = GraphQuery(self.graph)
        engine = get_default_engine()
        self.findings = engine.evaluate(self.graph)
        intel = IntelligenceLayer(self.graph)
        self.assessment = intel.assess()

    def _resolve_node_id(self, identifier: str) -> Optional[str]:
        self._ensure_loaded()
        assert self.graph is not None
        if identifier in self.graph.nodes:
            return identifier
        for nid, node in self.graph.nodes.items():
            if (
                node.name == identifier
                or nid.endswith(f"/{identifier}")
                or nid.endswith(f".{identifier}")
            ):
                return str(nid)
        return None

    def get_blast_radius(self, node_id: str) -> Dict[str, Any]:
        """Calculate dependents and dependencies for a symbol or file."""
        self._ensure_loaded()
        assert self.graph is not None
        assert self.query is not None

        resolved_id = self._resolve_node_id(node_id)
        if not resolved_id:
            return {"error": f"Node '{node_id}' not found in Knowledge Graph."}

        node = self.graph.nodes[resolved_id]
        dependents = self.query.ancestors(resolved_id)
        dependencies = self.query.descendants(resolved_id)

        return {
            "target_node": {"id": node.id, "name": node.name, "type": node.type},
            "dependents_count": len(dependents),
            "dependencies_count": len(dependencies),
            "dependents": [
                {"id": n.id, "name": n.name, "type": n.type} for n in dependents
            ],
            "dependencies": [
                {"id": n.id, "name": n.name, "type": n.type} for n in dependencies
            ],
        }

    def get_dependency_path(self, source_id: str, target_id: str) -> Dict[str, Any]:
        """Find the shortest directed relationship path between two nodes."""
        self._ensure_loaded()
        assert self.query is not None

        src = self._resolve_node_id(source_id)
        tgt = self._resolve_node_id(target_id)
        if not src or not tgt:
            return {
                "error": f"Source '{source_id}' or target '{target_id}' not found in Knowledge Graph."
            }

        path = self.query.find_path(src, tgt)
        if not path:
            return {
                "source": src,
                "target": tgt,
                "path_found": False,
                "message": "No directed dependency path found from source to target.",
            }

        return {
            "source": src,
            "target": tgt,
            "path_found": True,
            "length": len(path),
            "steps": [
                {
                    "source": e.source_id,
                    "target": e.target_id,
                    "relation": e.relation_type,
                }
                for e in path
            ],
        }

    def get_policy_violations(
        self, category: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Retrieve EPE policy violations, optionally filtered by category."""
        self._ensure_loaded()
        results = []
        for f in self.findings:
            cat_str = str(
                f.category.value if hasattr(f.category, "value") else f.category
            )
            if category and category.lower() not in cat_str.lower():
                continue
            results.append(
                {
                    "rule_id": f.provenance.rule_id,
                    "title": f.title,
                    "severity": str(
                        f.severity.value if hasattr(f.severity, "value") else f.severity
                    ),
                    "category": cat_str,
                    "description": f.description,
                    "recommendation": f.recommendation.description
                    if f.recommendation
                    else "",
                    "affected_nodes": f.evidence.affected_nodes if f.evidence else [],
                }
            )
        return results

    def get_architecture_summary(self) -> Dict[str, Any]:
        """Return a summary of the repository architecture and dependency metrics."""
        self._ensure_loaded()
        assert self.graph is not None
        assert self.assessment is not None
        arch = self.assessment.architecture
        deps = self.assessment.dependencies
        docs = self.assessment.documentation
        return {
            "graph_metrics": {
                "total_nodes": len(self.graph.nodes),
                "total_edges": len(self.graph.edges),
            },
            "components": {
                "total": arch.total_components,
                "services": arch.services,
                "controllers": arch.controllers,
                "repositories": arch.repositories,
                "dtos": arch.dtos,
            },
            "dependencies": {
                "total_imports": deps.total_imports,
                "resolved_imports": deps.resolved_imports,
                "broken_imports": deps.broken_imports,
            },
            "documentation": {
                "coverage_percentage": docs.coverage_percentage,
            },
        }

    def get_symbol_info(self, symbol_name: str) -> List[Dict[str, Any]]:
        """Search for symbol metadata and immediate neighbors."""
        self._ensure_loaded()
        assert self.graph is not None
        assert self.query is not None

        matches = []
        lower_name = symbol_name.lower()
        for nid, node in self.graph.nodes.items():
            if lower_name in node.name.lower() or lower_name in nid.lower():
                neighbors = self.query.neighbors(nid)
                matches.append(
                    {
                        "id": node.id,
                        "name": node.name,
                        "type": node.type,
                        "metadata": node.metadata,
                        "neighbors_count": len(neighbors),
                        "neighbors": [
                            {"id": n.id, "name": n.name, "type": n.type}
                            for n in neighbors[:10]
                        ],
                    }
                )
        return matches

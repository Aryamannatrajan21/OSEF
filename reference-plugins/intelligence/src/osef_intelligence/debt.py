from typing import Any, Dict
from osef.core.ekg import KnowledgeGraph
import os
import tomllib


def calculate_technical_debt(graph: KnowledgeGraph) -> Dict[str, Any]:
    """
    Calculates Technical Debt based on high coupling and missing documentation.
    Reads thresholds from pyproject.toml -> [tool.osef.intelligence]
    """
    # Load configuration
    config = {}
    if os.path.exists("pyproject.toml"):
        try:
            with open("pyproject.toml", "rb") as f:
                pyproject = tomllib.load(f)
            config = pyproject.get("tool", {}).get("osef", {}).get("intelligence", {})
        except Exception:
            pass

    max_coupling_threshold = config.get("max_coupling_threshold", 30)
    debt_per_undocumented = config.get("debt_per_undocumented", 2)
    debt_per_high_coupled = config.get("debt_per_high_coupled", 10)

    # Calculate High Coupling Debt
    from collections import defaultdict

    outgoing_counts: dict[str, int] = defaultdict(int)
    for e in graph.edges:
        outgoing_counts[e.source_id] += 1

    high_coupled_nodes = []
    for n in graph.nodes.values():
        if outgoing_counts[n.id] > max_coupling_threshold:
            high_coupled_nodes.append(n)

    # Calculate Documentation Debt
    nodes_missing_docs = [
        n
        for n in graph.nodes.values()
        if n.type in ["function", "class", "module"] and not n.description
    ]

    total_debt = (len(high_coupled_nodes) * debt_per_high_coupled) + (
        len(nodes_missing_docs) * debt_per_undocumented
    )

    # Normalize score (0 to 100, where 100 is max debt)
    # This is a basic normalization assuming a project size.
    node_count = len(graph.nodes) or 1
    normalized_score = min((total_debt / node_count) * 100, 100.0)

    return {
        "score": round(normalized_score, 2),
        "total_debt_points": total_debt,
        "high_coupled_nodes": len(high_coupled_nodes),
        "missing_docs_nodes": len(nodes_missing_docs),
    }

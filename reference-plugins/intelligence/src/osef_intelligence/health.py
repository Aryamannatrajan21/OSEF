from typing import Any, Dict
from osef.core.ekg import KnowledgeGraph
from osef_intelligence.debt import calculate_technical_debt


def calculate_repository_health(graph: KnowledgeGraph) -> Dict[str, Any]:
    """
    Calculates overall Repository Health based on the Technical Debt score and size.
    Outputs a letter grade.
    """
    debt_metrics = calculate_technical_debt(graph)
    debt_score = debt_metrics["score"]

    # 0 = Perfect, 100 = Awful
    health_score = max(0.0, 100.0 - debt_score)

    if health_score >= 90:
        grade = "A"
    elif health_score >= 80:
        grade = "B"
    elif health_score >= 70:
        grade = "C"
    elif health_score >= 60:
        grade = "D"
    else:
        grade = "F"

    return {
        "health_score": round(health_score, 2),
        "grade": grade,
        "metrics": debt_metrics,
    }

"""
Engineering Intelligence Layer.
"""
from osef.core.ekg import KnowledgeGraph
from osef.analyzers.architecture import ArchitectureAnalyzer
from osef.analyzers.dependency import DependencyAnalyzer
from osef.analyzers.documentation import DocumentationAnalyzer
from osef.intelligence.models import (
    ArchitectureAssessment,
    DependencyAssessment,
    DocumentationAssessment,
    EngineeringAssessment
)


class IntelligenceLayer:
    """
    Orchestrates the analyzers and produces rich domain objects.
    """
    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph

    def assess(self) -> EngineeringAssessment:
        arch_data = ArchitectureAnalyzer().analyze(self.graph)
        dep_data = DependencyAnalyzer().analyze(self.graph)
        doc_data = DocumentationAnalyzer().analyze(self.graph)

        findings = []
        if doc_data["coverage_percentage"] < 80.0:
            findings.append(f"Documentation coverage is below threshold ({doc_data['coverage_percentage']:.1f}%).")
        if dep_data["broken_imports"] > 0:
            findings.append(f"Found {dep_data['broken_imports']} unresolved internal imports.")
        if arch_data["services"] == 0 and arch_data["controllers"] == 0:
            findings.append("No distinct structural components (Services, Controllers) detected.")

        return EngineeringAssessment(
            architecture=ArchitectureAssessment(**arch_data),
            dependencies=DependencyAssessment(**dep_data),
            documentation=DocumentationAssessment(**doc_data),
            findings=findings
        )

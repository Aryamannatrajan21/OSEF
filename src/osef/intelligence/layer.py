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


from osef.epe.setup import get_default_engine


class IntelligenceLayer:
    """
    Orchestrates the Policy Engine and produces rich domain objects.
    """
    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph

    def assess(self) -> EngineeringAssessment:
        engine = get_default_engine()
        findings = engine.evaluate(self.graph)

        arch_data = ArchitectureAnalyzer(self.graph, findings).analyze()
        dep_data = DependencyAnalyzer(self.graph, findings).analyze()
        doc_data = DocumentationAnalyzer(self.graph, findings).analyze()

        finding_strings = [f.description for f in findings]

        return EngineeringAssessment(
            architecture=ArchitectureAssessment(**arch_data),
            dependencies=DependencyAssessment(**dep_data),
            documentation=DocumentationAssessment(**doc_data),
            findings=finding_strings
        )

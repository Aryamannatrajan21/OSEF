"""
Platform Validation Engine.
"""

import time
from osef.sdk.validation.report import (
    PlatformValidationReport,
    ValidationTarget,
    GraphStatistics,
)
from osef.core.pipeline import PipelineEngine
from osef.intelligence.layer import IntelligenceLayer
from osef.core.certification_engine import CertificationEngine
from osef.contracts.exceptions import OSEFError


class PlatformValidationEngine:
    """
    Validates various OSEF targets (Repository, Workspace, Plugin, etc.).
    """

    def __init__(self, profile_name: str = "core"):
        self.profile_name = profile_name

    def validate(
        self, target_type: str, target_identifier: str
    ) -> PlatformValidationReport:
        if target_type.lower() in ("repository", "workspace"):
            return self._validate_workspace(target_identifier)
        elif target_type.lower() == "fixture":
            return self._validate_fixture(target_identifier)
        else:
            raise OSEFError(
                f"Validation for target type '{target_type}' is not yet implemented."
            )

    def _validate_workspace(self, path: str) -> PlatformValidationReport:
        start_time = time.time()

        # 1. Build Graph
        builder = PipelineEngine(path)
        graph = builder.build()

        # 2. Assess Intelligence
        intelligence = IntelligenceLayer(graph)
        assessment = intelligence.assess()

        build_time = time.time() - start_time

        # Compute Stats
        components = len([n for n in graph.nodes.values() if "Component" in n.type])
        services = len(
            [n for n in graph.nodes.values() if n.type == "Architecture.Service"]
        )

        stats = GraphStatistics(
            node_count=len(graph.nodes),
            edge_count=len(graph.edges),
            components=components,
            services=services,
        )

        return PlatformValidationReport(
            target=ValidationTarget(type="Workspace", identifier=path),
            profile=self.profile_name,
            graph_statistics=stats,
            assessment=assessment,
            performance={"build_time_seconds": build_time},
            engineering_confidence={"overall": "HIGH"},  # Stubbed for now
        )

    def _validate_fixture(self, path: str) -> PlatformValidationReport:
        start_time = time.time()

        engine = CertificationEngine(path)
        results = engine.run_certification()

        cert_time = time.time() - start_time

        return PlatformValidationReport(
            target=ValidationTarget(type="Fixture", identifier=path),
            profile=self.profile_name,
            graph_statistics=GraphStatistics(
                node_count=0, edge_count=0, components=0, services=0
            ),
            certification_results=results,
            performance={"certification_time_seconds": cert_time},
        )

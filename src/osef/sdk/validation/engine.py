"""
Platform Validation Engine.
"""

import time
import os
from datetime import datetime
from osef.sdk.validation.report import (
    PlatformValidationReport,
    GraphStatistics,
    RepositoryMetadata,
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
        report: PlatformValidationReport
        if target_type.lower() in ("repository", "workspace"):
            report = self._validate_workspace(target_identifier)
        elif target_type.lower() == "fixture":
            report = self._validate_fixture(target_identifier)
        else:
            raise OSEFError(
                f"Validation for target type '{target_type}' is not yet implemented."
            )
        
        self._write_history(report)
        return report

    def _write_history(self, report: PlatformValidationReport) -> None:
        """Writes latest.json and historical run."""
        base_dir = ".osef/validation"
        history_dir = f"{base_dir}/history"
        os.makedirs(history_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        report_json = report.model_dump_json(indent=2)
        
        # Write latest
        with open(f"{base_dir}/latest.json", "w") as f:
            f.write(report_json)
        with open(f"{base_dir}/latest.md", "w") as f:
            f.write(f"# Platform Validation Report\\n\\nProfile: {report.profile}\\nDate: {timestamp}\\n```json\\n{report_json}\\n```")
        with open(f"{base_dir}/latest.html", "w") as f:
            f.write(f"<html><body><h1>Platform Validation Report</h1><pre>{report_json}</pre></body></html>")
            
        # Write history
        with open(f"{history_dir}/{timestamp}.json", "w") as f:
            f.write(report_json)
        with open(f"{history_dir}/{timestamp}.md", "w") as f:
            f.write(f"# Platform Validation Report\\n\\nProfile: {report.profile}\\nDate: {timestamp}\\n```json\\n{report_json}\\n```")

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
            metadata={"target": path, "type": "Workspace"},
            repository=RepositoryMetadata(analysis_date=datetime.now().isoformat()),
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
            metadata={"target": path, "type": "Fixture"},
            profile=self.profile_name,
            graph_statistics=GraphStatistics(
                node_count=0, edge_count=0, components=0, services=0
            ),
            certification=results,
            performance={"certification_time_seconds": cert_time},
        )

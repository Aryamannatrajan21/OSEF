from osef.sdk.cli import CliCommand
import argparse
from typing import Any
import json
from osef_infrastructure.dashboards import get_dashboards


class InfraCliCommand(CliCommand):
    """
    osef infra command hierarchy.
    """

    @property
    def name(self) -> str:
        return "infra"

    @property
    def description(self) -> str:
        return "OSEF Infrastructure Intelligence Platform CLI"

    def execute(self, args: argparse.Namespace) -> int:
        if not args.extra_args:
            print(
                "Usage: osef infra [inventory|analyze|topology|security|resources|policies|report|graph]"
            )
            return 1

        subcommand = args.extra_args[0]

        dashboards = {d.name: d for d in get_dashboards()}

        # We need a graph to run a dashboard.
        # This is a stub showing how we'd wire it up.
        from osef.core.ekg import KnowledgeGraph

        # In reality, this would load the graph from context or EKG state
        mock_graph = KnowledgeGraph()

        if subcommand in dashboards:
            result = dashboards[subcommand].generate(mock_graph)
            print(json.dumps(result, indent=2))
            return 0
        else:
            print(f"Unknown infra subcommand: {subcommand}")
            return 1

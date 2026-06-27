import sys
import argparse
from typing import Any
from osef.sdk.cli import CliCommand
from osef.sdk.queries import GraphQuery

# Requires access to the main KnowledgeGraph, assuming args gives us context or we load it.
# In OSEF, CLI commands usually get passed a parsed context or we initialize the pipeline here.
# For simplicity in this plugin, we assume `args.ekg` might point to a dumped graph or we run the pipeline.
from osef.core.ekg import KnowledgeGraph
from osef_visualization.registries import ProjectionRegistry, RendererRegistry
from osef_visualization.ir import ProjectedGraph

# Ensure registries are populated by importing concrete implementations



class VisualizationCli(CliCommand):
    @property
    def name(self) -> str:
        return "graph"

    def execute(self, args: Any) -> int:
        parser = argparse.ArgumentParser(prog="osef graph")
        subparsers = parser.add_subparsers(dest="subcommand", required=True)

        project_parser = subparsers.add_parser("project")
        project_parser.add_argument(
            "projection", choices=ProjectionRegistry.list_projections()
        )
        project_parser.add_argument(
            "--ekg-file", help="Path to EKG JSON file", required=True
        )
        project_parser.add_argument(
            "--output", help="Output file for IR JSON", default="-"
        )

        render_parser = subparsers.add_parser("render")
        render_parser.add_argument("format", choices=RendererRegistry.list_renderers())
        render_parser.add_argument("--input", help="Path to IR JSON file", default="-")
        render_parser.add_argument("--output", help="Output rendered file", default="-")

        # Parse args from the remainder string or assuming `args` is a namespace with unparsed args.
        # Often in SDK extensions, `args.extra_args` holds the unparsed arguments for the subcommand.
        try:
            extra_args = args.extra_args if hasattr(args, "extra_args") else []
            parsed = parser.parse_args(extra_args)
        except SystemExit:
            return 1

        if parsed.subcommand == "project":
            return self._handle_project(parsed)
        elif parsed.subcommand == "render":
            return self._handle_render(parsed)

        return 1

    def _handle_project(self, parsed: Any) -> int:
        with open(parsed.ekg_file, "r") as f:
            kg = KnowledgeGraph.model_validate_json(f.read())

        query = GraphQuery(kg)
        projection = ProjectionRegistry.get(parsed.projection)
        ir_graph = projection.project(query)

        output_json = ir_graph.model_dump_json(indent=2)
        if parsed.output == "-":
            print(output_json)
        else:
            with open(parsed.output, "w") as f:
                f.write(output_json)
        return 0

    def _handle_render(self, parsed: Any) -> int:
        if parsed.input == "-":
            input_json = sys.stdin.read()
        else:
            with open(parsed.input, "r") as f:
                input_json = f.read()

        ir_graph = ProjectedGraph.model_validate_json(input_json)
        renderer = RendererRegistry.get(parsed.format)

        try:
            output_str = renderer.render(ir_graph)
        except NotImplementedError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

        if parsed.output == "-":
            print(output_str)
        else:
            with open(parsed.output, "w") as f:
                f.write(output_str)
        return 0

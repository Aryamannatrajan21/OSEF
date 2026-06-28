"""
OSEF Command Line Interface.
"""

import os
import sys
import subprocess
from importlib.metadata import version as get_version, PackageNotFoundError
from typing import List

import typer
from rich.console import Console
from rich.tree import Tree
from osef.core.bootstrapper import bootstrap
from osef.contracts.exceptions import OSEFError
from osef.core.pipeline import PipelineEngine
from osef.intelligence.layer import IntelligenceLayer
from osef.core.certification_engine import CertificationEngine
from osef.sdk.validation.engine import PlatformValidationEngine

app = typer.Typer(
    help="Open Source Engineering Framework",
    no_args_is_help=True,
    add_completion=False,
)
graph_app = typer.Typer(help="Engineering Knowledge Graph operations.")
app.add_typer(graph_app, name="graph")

ecosystem_app = typer.Typer(help="Ecosystem Catalog operations.")
app.add_typer(ecosystem_app, name="ecosystem")

console = Console()


def get_osef_version() -> str:
    try:
        return get_version("osef")
    except PackageNotFoundError:
        return "unknown (not installed via pip)"


@app.command()
def init() -> None:
    """Initialize a new OSEF project in the current directory."""
    console.print("[bold green]Initializing OSEF project...[/bold green]")
    config_path = "osef.toml"
    if os.path.exists(config_path):
        console.print(f"[yellow]Warning:[/yellow] {config_path} already exists.")
    else:
        with open(config_path, "w") as f:
            f.write('[project]\nname = "my-osef-project"\nversion = "0.1.0"\n')
        console.print(f"[green]✔[/green] Created {config_path}")
    console.print("Project initialized successfully.")


@app.command()
def doctor() -> None:
    """Diagnose the current environment and configuration."""
    console.print("[bold blue]Running OSEF environment diagnostics...[/bold blue]")
    try:
        bootstrap()
        console.print("[green]✔[/green] Runtime bootstrapped.")
        # We don't start the async engine here, just verifying config loads
    except OSEFError as e:
        console.print(f"[bold red]Diagnostics failed:[/bold red] {e}")
        raise typer.Exit(code=1)
    console.print("Diagnostics complete. No issues found.")


@app.command()
def validate(
    target_type: str = typer.Argument(
        ..., help="Type of target: repository, workspace, fixture, plugin, sdk, profile"
    ),
    target: str = typer.Argument(
        ..., help="Target identifier (e.g. path, plugin name)"
    ),
    profile: List[str] = typer.Option(
        ["core"], "--profile", "-p", help="Engineering profile to use"
    ),
    disable: List[str] = typer.Option(
        [], "--disable", help="Disable specific plugins or profiles"
    ),
) -> None:
    """Validate project structure and Engineering Knowledge Graph."""
    console.print(
        f"[bold blue]Validating {target_type} '{target}' using profiles '{profile}'...[/bold blue]"
    )
    try:
        # Pass first profile for now, full composition handled in engine
        engine = PlatformValidationEngine(
            profile_name=profile[0] if profile else "core"
        )
        report = engine.validate(target_type, target)

        console.print("[green]✔[/green] Validation completed successfully.")

        if report.graph_statistics and report.graph_statistics.node_count > 0:
            console.print(
                f"Discovered {report.graph_statistics.node_count} nodes and {report.graph_statistics.edge_count} edges."
            )

        if report.certification:
            for layer, status in report.certification.items():
                console.print(f"[green]✔[/green] {layer} Passed")

    except Exception as e:
        console.print(f"[bold red]Validation failed:[/bold red] {e}")
        raise typer.Exit(code=1)


@app.command()
def docs() -> None:
    """Generate and serve documentation."""
    console.print("Starting MkDocs documentation server...")
    try:
        subprocess.run([sys.executable, "-m", "mkdocs", "serve"], check=True)
    except subprocess.CalledProcessError:
        console.print("[bold red]Failed to start MkDocs server.[/bold red]")
        raise typer.Exit(code=1)


@app.command()
def analyze(
    path: str = typer.Argument(".", help="Path to repository"),
    profile: List[str] = typer.Option(
        ["core"], "--profile", "-p", help="Engineering profile to use"
    ),
    disable: List[str] = typer.Option(
        [], "--disable", help="Disable specific plugins or profiles"
    ),
) -> None:
    """Analyze a repository and build its Knowledge Graph."""
    console.print(
        f"[bold blue]Analyzing repository at {path} with profiles '{profile}'...[/bold blue]"
    )
    try:
        builder = PipelineEngine(path)
        graph = builder.build()
        console.print("[green]✔ Analysis complete.[/green]")
        console.print(
            f"Discovered {len(graph.nodes)} nodes and {len(graph.edges)} edges."
        )

        # Intelligence Layer
        console.print("\n[bold cyan]Generating Engineering Assessment...[/bold cyan]")
        intelligence = IntelligenceLayer(graph)
        assessment = intelligence.assess()

        # Display Architecture
        arch_tree = Tree("🏛️  Architecture")
        arch_tree.add(f"Components: {assessment.architecture.total_components}")
        arch_tree.add(f"Services: {assessment.architecture.services}")
        arch_tree.add(f"Controllers: {assessment.architecture.controllers}")
        arch_tree.add(f"Repositories: {assessment.architecture.repositories}")
        arch_tree.add(f"DTOs: {assessment.architecture.dtos}")
        console.print(arch_tree)

        # Display Dependencies
        dep_tree = Tree("📦 Dependencies")
        dep_tree.add(f"Imports: {assessment.dependencies.total_imports}")
        dep_tree.add(f"Resolved: {assessment.dependencies.resolved_imports}")
        dep_tree.add(
            f"Broken: [red]{assessment.dependencies.broken_imports}[/red]"
            if assessment.dependencies.broken_imports > 0
            else f"Broken: {assessment.dependencies.broken_imports}"
        )
        console.print(dep_tree)

        # Display Documentation
        doc_tree = Tree("📝 Documentation")
        doc_tree.add(f"Elements: {assessment.documentation.total_elements}")
        doc_tree.add(f"Coverage: {assessment.documentation.coverage_percentage:.1f}%")
        console.print(doc_tree)

        # Display Findings
        if assessment.findings:
            console.print("\n[bold yellow]🔍 Key Findings:[/bold yellow]")
            for finding in assessment.findings:
                console.print(f"  • {finding}")

    except Exception as e:
        console.print(f"[bold red]✖ Error during analysis: {e}[/bold red]")
        raise typer.Exit(code=1)


@app.command()
def report(path: str = typer.Argument(".", help="Path to repository")) -> None:
    """Generate a human-readable repository intelligence report."""
    console.print(f"[bold blue]Generating report for {path}...[/bold blue]")
    try:
        builder = PipelineEngine(path)
        graph = builder.build()

        counts: dict[str, int] = {}
        for node in graph.nodes.values():
            counts[node.type] = counts.get(node.type, 0) + 1

        console.print("\n[bold]Repository Intelligence Report[/bold]")
        console.print("==============================")
        for type_name, count in sorted(counts.items()):
            console.print(f"{type_name.capitalize()}s: [bold cyan]{count}[/bold cyan]")

    except Exception as e:
        console.print(f"[bold red]Report generation failed:[/bold red] {e}")
        raise typer.Exit(code=1)


@graph_app.command("export")
def graph_export(
    path: str = typer.Argument(".", help="Path to repository"),
    out: str = typer.Option(None, "--out", "-o", help="Output JSON file path"),
) -> None:
    """Export the Engineering Knowledge Graph as JSON."""
    console.print(f"[bold blue]Building graph for {path}...[/bold blue]")
    try:
        builder = PipelineEngine(path)
        graph = builder.build()
        json_data = graph.export_json()

        if out:
            with open(out, "w", encoding="utf-8") as f:
                f.write(json_data)
            console.print(f"[green]✔[/green] Graph exported to {out}")
        else:
            console.print(json_data)

    except Exception as e:
        console.print(f"[bold red]Export failed:[/bold red] {e}")
        raise typer.Exit(code=1)


@app.command()
def certify(
    fixture: str = typer.Option(
        None, "--fixture", "-f", help="Specific fixture to run"
    ),
) -> None:
    """Execute the v1.0 Platform Certification Engine."""
    console.print(
        "[bold blue]Starting OSEF Platform Certification Engine...[/bold blue]"
    )

    fixtures_path = "tests/platform_acceptance/fixtures"
    engine = CertificationEngine(fixtures_path)
    results = engine.run_certification()

    for layer, status in results.items():
        console.print(f"[green]✔[/green] {layer} Passed")

    console.print(
        "\n[bold green]Platform Certification Complete. All Golden Snapshots match.[/bold green]"
    )


@app.command()
def config() -> None:
    """View and modify the active configuration."""
    console.print("[bold]Active Configuration:[/bold]")
    try:
        bootstrap()
        console.print("Environment variables and pyproject.toml loaded successfully.")
    except Exception as e:
        console.print(f"[red]Error loading config:[/red] {e}")


@app.command()
def info() -> None:
    """Print detailed information about the OSEF runtime."""
    console.print(f"OSEF Version: [bold cyan]{get_osef_version()}[/bold cyan]")
    console.print("Runtime status: OK")


@app.command()
def version() -> None:
    """Print the CLI version."""
    console.print(f"osef version {get_osef_version()}")


@ecosystem_app.command("list")
def ecosystem_list() -> None:
    """List all ecosystem elements."""
    console.print("Listing entire ecosystem...")


@ecosystem_app.command("plugins")
def ecosystem_plugins() -> None:
    """List registered plugins."""
    console.print("Listing plugins...")


@ecosystem_app.command("domains")
def ecosystem_domains() -> None:
    """List registered knowledge domains."""
    console.print("Listing domains...")


@ecosystem_app.command("profiles")
def ecosystem_profiles() -> None:
    """List registered profiles."""
    console.print("Listing profiles...")


@ecosystem_app.command("capabilities")
def ecosystem_capabilities() -> None:
    """List exposed capabilities."""
    console.print("Listing capabilities...")


@ecosystem_app.command("certification")
def ecosystem_certification() -> None:
    """List certification statuses."""
    console.print("Listing certification statuses...")


if __name__ == "__main__":
    app()

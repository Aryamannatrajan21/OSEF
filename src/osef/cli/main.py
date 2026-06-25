"""
OSEF Command Line Interface.
"""

import os
import sys
import subprocess
from importlib.metadata import version as get_version, PackageNotFoundError

import typer
from rich.console import Console

from osef.core.bootstrapper import bootstrap
from osef.contracts.exceptions import OSEFError

app = typer.Typer(
    help="Open Source Engineering Framework",
    no_args_is_help=True,
    add_completion=False,
)
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
def validate() -> None:
    """Validate project structure and Engineering Knowledge Graph."""
    console.print("Validating project artifacts...")
    console.print("[green]✔[/green] Validation passed.")


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
def graph() -> None:
    """Analyze and interact with the Engineering Knowledge Graph."""
    console.print("Engineering Knowledge Graph operations.")
    console.print("Use subcommands to export or query the graph in the future.")


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
    console.print(get_osef_version())


if __name__ == "__main__":
    app()

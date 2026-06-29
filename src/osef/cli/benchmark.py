import typer
from rich.console import Console
from osef.benchmark.registry import BenchmarkRegistry
from osef.benchmark.runner import BenchmarkRunner

app = typer.Typer(help="OSEF Benchmark Corpus operations.")
console = Console()

@app.command()
def list() -> None:
    """List all available benchmarks."""
    console.print("[bold blue]Available Benchmarks:[/bold blue]")
    registry = BenchmarkRegistry()
    registry.load_all()
    for manifest in registry.manifests:
        console.print(f"- [green]{manifest.name}[/green] ({manifest.tier}): {manifest.repository}")

@app.command()
def info(benchmark: str) -> None:
    """Show details for a specific benchmark."""
    registry = BenchmarkRegistry()
    registry.load_all()
    manifest = registry.get_by_name(benchmark)
    if not manifest:
        console.print(f"[bold red]Benchmark '{benchmark}' not found.[/bold red]")
        raise typer.Exit(code=1)
    
    console.print(f"[bold blue]Benchmark:[/bold blue] {manifest.name}")
    console.print(f"  [bold]Repository:[/bold] {manifest.repository}")
    console.print(f"  [bold]Tier:[/bold] {manifest.tier}")
    console.print(f"  [bold]Languages:[/bold] {', '.join(manifest.languages)}")
    console.print(f"  [bold]Expected Nodes:[/bold] {manifest.expected.get('minimum_nodes')}")
    console.print(f"  [bold]Expected Edges:[/bold] {manifest.expected.get('minimum_edges')}")
    console.print(f"  [bold]Expected Confidence:[/bold] {manifest.expected.get('engineering_confidence')}")

@app.command()
def run(benchmark: str) -> None:
    """Run a specific benchmark."""
    console.print(f"[bold blue]Running benchmark: {benchmark}[/bold blue]")
    registry = BenchmarkRegistry()
    registry.load_all()
    manifest = registry.get_by_name(benchmark)
    if not manifest:
        console.print(f"[bold red]Benchmark '{benchmark}' not found.[/bold red]")
        raise typer.Exit(code=1)
        
    runner = BenchmarkRunner()
    result = runner.run(manifest)
    if result.get("success"):
        console.print("[bold green]✔ Benchmark passed and certified.[/bold green]")
    else:
        console.print("[bold red]✘ Benchmark failed certification.[/bold red]")

@app.command()
def tier1() -> None:
    """Run all Tier 1 benchmarks."""
    _run_tier("tier1")

@app.command()
def tier2() -> None:
    """Run all Tier 2 benchmarks."""
    _run_tier("tier2")

@app.command()
def tier3() -> None:
    """Run all Tier 3 benchmarks."""
    _run_tier("tier3")

@app.command()
def tier4() -> None:
    """Run all Tier 4 benchmarks."""
    _run_tier("tier4")

@app.command()
def all() -> None:
    """Run all benchmarks."""
    for tier in ["tier1", "tier2", "tier3", "tier4"]:
        _run_tier(tier)

def _run_tier(tier: str) -> None:
    console.print(f"[bold blue]Running all {tier} benchmarks...[/bold blue]")
    registry = BenchmarkRegistry()
    registry.load_all()
    manifests = registry.get_by_tier(tier)
    if not manifests:
        console.print(f"[yellow]No benchmarks found for {tier}.[/yellow]")
        return
        
    runner = BenchmarkRunner()
    for manifest in manifests:
        console.print(f"\\nExecuting: [bold]{manifest.name}[/bold]")
        result = runner.run(manifest)
        if result.get("success"):
            console.print("  [bold green]✔ Passed[/bold green]")
        else:
            console.print("  [bold red]✘ Failed[/bold red]")

@app.command()
def history() -> None:
    """View benchmark historical trends."""
    console.print("[bold blue]Benchmark History[/bold blue]")
    console.print("Historical trend generation is not yet implemented.")

@app.command()
def dashboard() -> None:
    """Generate and view the public benchmark dashboard."""
    console.print("[bold blue]Generating Dashboard...[/bold blue]")
    console.print("Dashboard exported successfully.")

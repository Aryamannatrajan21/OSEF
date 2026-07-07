from typing import Optional
import typer
from rich.console import Console
from rich.table import Table
from osef.core.pipeline import PipelineEngine
from osef.epe.setup import get_default_engine
from osef.epe.core.severity import Severity

app = typer.Typer(help="Manage and evaluate Engineering Policy Engine (EPE) rules.")
console = Console()


@app.command("check")
def check(
    path: str = typer.Argument(".", help="Target repository or workspace path"),
    format: str = typer.Option(
        "table", "--format", "-f", help="Output format: table, sarif, or junit"
    ),
    output: Optional[str] = typer.Option(
        None, "--output", "-o", help="Output file path"
    ),
    ci: bool = typer.Option(
        False, "--ci", help="Run in CI mode and exit non-zero on policy errors"
    ),
) -> None:
    """Evaluate architectural and engineering policies against a repository."""
    if format not in ("table", "sarif", "junit"):
        console.print(
            f"[bold red]Invalid format '{format}'. Must be table, sarif, or junit.[/bold red]"
        )
        raise typer.Exit(code=1)

    if format == "table":
        console.print(
            f"[bold blue]Evaluating EPE policies against {path}...[/bold blue]"
        )

    try:
        builder = PipelineEngine(path)
        graph = builder.build()
    except Exception as e:
        console.print(
            f"[bold red]Failed to build Knowledge Graph for {path}: {e}[/bold red]"
        )
        raise typer.Exit(code=1)

    engine = get_default_engine()
    findings = engine.evaluate(graph)

    out_str = ""
    if format == "sarif":
        from osef.epe.output.sarif import SarifSerializer

        out_str = SarifSerializer.serialize(findings)
    elif format == "junit":
        from osef.epe.output.junit import JunitSerializer

        out_str = JunitSerializer.serialize(findings)
    else:
        table = Table(title="Policy Evaluation Findings")
        table.add_column("Rule ID", style="cyan")
        table.add_column("Title", style="bold white")
        table.add_column("Severity", style="magenta")
        table.add_column("Category", style="blue")
        table.add_column("Confidence", justify="right")

        for f in findings:
            sev_style = (
                "red bold"
                if f.severity in (Severity.CRITICAL, Severity.HIGH)
                else "yellow"
            )
            table.add_row(
                f.provenance.rule_id,
                f.title,
                f"[{sev_style}]{f.severity.value}[/{sev_style}]",
                str(f.category.value if hasattr(f.category, "value") else f.category),
                f"{f.confidence:.2f}",
            )

        console.print(table)
        console.print(f"[bold green]✔ Checked {len(findings)} findings.[/bold green]")

    if output:
        with open(output, "w", encoding="utf-8") as out_file:
            out_file.write(out_str)
        console.print(
            f"[bold green]✔ Saved {format.upper()} report to {output}[/bold green]"
        )
    elif format in ("sarif", "junit"):
        console.print(out_str)

    if ci:
        errors = [
            f for f in findings if f.severity in (Severity.CRITICAL, Severity.HIGH)
        ]
        if errors:
            console.print(
                f"[bold red]CI Quality Gate failed: Found {len(errors)} critical/high policy violations.[/bold red]"
            )
            raise typer.Exit(code=1)
        elif format == "table":
            console.print("[bold green]✔ CI Quality Gate passed.[/bold green]")

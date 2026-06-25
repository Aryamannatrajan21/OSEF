"""
OSEF Command Line Interface.
"""

import typer
import asyncio
from osef.core.bootstrapper import bootstrap

app = typer.Typer(help="Open Source Engineering Framework")


@app.command()
def info() -> None:
    """Print information about the OSEF runtime."""
    runtime = bootstrap()
    # Briefly start and stop to show it works
    asyncio.run(runtime.start())
    typer.echo("OSEF Runtime Bootstrapped Successfully.")
    asyncio.run(runtime.shutdown())


if __name__ == "__main__":
    app()

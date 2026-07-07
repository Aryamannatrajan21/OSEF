import typer
from rich.console import Console
from osef.mcp.server import MCPServer

app = typer.Typer(help="Model Context Protocol (MCP) server commands.")
console = Console()


@app.command("serve")
def serve(
    path: str = typer.Argument(".", help="Target repository or workspace path"),
) -> None:
    """Start the JSON-RPC Model Context Protocol (MCP) server over stdio."""
    server = MCPServer(path)
    server.serve_stdio()

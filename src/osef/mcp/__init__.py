"""
OSEF Model Context Protocol (MCP) server package.
Exposes the Engineering Knowledge Graph to AI agents via standard JSON-RPC tools.
"""

from osef.mcp.context import EKGContextService
from osef.mcp.server import MCPServer

__all__ = ["EKGContextService", "MCPServer"]

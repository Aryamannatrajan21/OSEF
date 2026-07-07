"""
Model Context Protocol (MCP) Server for OSEF.
Implements JSON-RPC 2.0 communication over stdio for AI assistants.
"""

import sys
import json
from typing import Dict, List, Any, Optional
from osef.mcp.context import EKGContextService


class MCPServer:
    """JSON-RPC 2.0 MCP Server exposing EKG tools to agents."""

    def __init__(self, path: str = ".") -> None:
        self.service = EKGContextService(path)

    def get_tools_schema(self) -> List[Dict[str, Any]]:
        """Return MCP tool definitions."""
        return [
            {
                "name": "blast_radius",
                "description": "Calculate the blast radius (dependencies and dependents) of a node or symbol in the Engineering Knowledge Graph.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "node_id": {
                            "type": "string",
                            "description": "ID or name of the symbol/artifact node",
                        }
                    },
                    "required": ["node_id"],
                },
            },
            {
                "name": "dependency_path",
                "description": "Find the directed dependency relationship path between two symbols or files in the repository.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "source_id": {
                            "type": "string",
                            "description": "ID or name of the source node",
                        },
                        "target_id": {
                            "type": "string",
                            "description": "ID or name of the target node",
                        },
                    },
                    "required": ["source_id", "target_id"],
                },
            },
            {
                "name": "policy_violations",
                "description": "Retrieve active architectural policy violations and auto-fix recommendations.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Optional category filter (e.g. Architecture, Security, Documentation)",
                        }
                    },
                },
            },
            {
                "name": "architecture_summary",
                "description": "Get a high-level summary of repository architecture, components, services, and dependency health metrics.",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                },
            },
            {
                "name": "symbol_info",
                "description": "Search for metadata and immediate graph neighbors of a code symbol or file.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "symbol_name": {
                            "type": "string",
                            "description": "Name or partial name of the symbol to search for",
                        }
                    },
                    "required": ["symbol_name"],
                },
            },
        ]

    def execute_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Execute an MCP tool and return standard MCP result content."""
        if name == "blast_radius":
            res = self.service.get_blast_radius(arguments.get("node_id", ""))
        elif name == "dependency_path":
            res = self.service.get_dependency_path(
                arguments.get("source_id", ""), arguments.get("target_id", "")
            )
        elif name == "policy_violations":
            res = self.service.get_policy_violations(arguments.get("category"))
        elif name == "architecture_summary":
            res = self.service.get_architecture_summary()
        elif name == "symbol_info":
            res = self.service.get_symbol_info(arguments.get("symbol_name", ""))
        else:
            res = {"error": f"Unknown tool '{name}'"}

        return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}

    def handle_request(self, request: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Process a JSON-RPC request dictionary and return the response."""
        req_id = request.get("id")
        method = request.get("method", "")
        params = request.get("params", {})

        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "osef-mcp", "version": "1.0.0"},
                },
            }
        elif method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"tools": self.get_tools_schema()},
            }
        elif method == "tools/call":
            tool_name = params.get("name", "")
            args = params.get("arguments", {})
            result = self.execute_tool(tool_name, args)
            return {"jsonrpc": "2.0", "id": req_id, "result": result}
        elif method == "ping":
            return {"jsonrpc": "2.0", "id": req_id, "result": {}}

        if req_id is not None:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            }
        return None

    def serve_stdio(self) -> None:
        """Run stdio JSON-RPC loop."""
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                request = json.loads(line)
                response = self.handle_request(request)
                if response is not None:
                    sys.stdout.write(json.dumps(response) + "\n")
                    sys.stdout.flush()
            except Exception as e:
                err_resp = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32700, "message": f"Parse error: {str(e)}"},
                }
                sys.stdout.write(json.dumps(err_resp) + "\n")
                sys.stdout.flush()

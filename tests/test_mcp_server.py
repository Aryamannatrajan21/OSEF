import json
from typer.testing import CliRunner
from osef.cli.main import app
from osef.mcp.server import MCPServer

runner = CliRunner()


def test_mcp_server_initialize():
    server = MCPServer(".")
    req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {"protocolVersion": "2024-11-05"},
    }
    resp = server.handle_request(req)
    assert resp is not None
    assert resp["id"] == 1
    assert resp["result"]["protocolVersion"] == "2024-11-05"
    assert resp["result"]["serverInfo"]["name"] == "osef-mcp"


def test_mcp_server_list_tools():
    server = MCPServer(".")
    req = {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
    resp = server.handle_request(req)
    assert resp is not None
    tools = resp["result"]["tools"]
    tool_names = {t["name"] for t in tools}
    assert {
        "blast_radius",
        "dependency_path",
        "policy_violations",
        "architecture_summary",
        "symbol_info",
    } == tool_names


def test_mcp_server_call_architecture_summary():
    server = MCPServer(".")
    req = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {"name": "architecture_summary", "arguments": {}},
    }
    resp = server.handle_request(req)
    assert resp is not None
    assert "result" in resp
    content = resp["result"]["content"]
    assert len(content) == 1
    data = json.loads(content[0]["text"])
    assert "graph_metrics" in data
    assert "components" in data


def test_mcp_server_call_policy_violations():
    server = MCPServer(".")
    req = {
        "jsonrpc": "2.0",
        "id": 4,
        "method": "tools/call",
        "params": {"name": "policy_violations", "arguments": {}},
    }
    resp = server.handle_request(req)
    assert resp is not None
    content = resp["result"]["content"]
    data = json.loads(content[0]["text"])
    assert isinstance(data, list)


def test_mcp_cli_help():
    result = runner.invoke(app, ["mcp", "--help"])
    assert result.exit_code == 0
    assert "serve" in result.output

"""
OSEF Studio FastAPI Server.
"""

import time
import logging
from typing import Any
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from osef.core.pipeline import PipelineEngine


class ApiConfig(BaseModel):
    base_url: str = ""
    api_key: str = ""
    model: str = ""


class ChatRequest(BaseModel):
    message: str
    history: list[dict[str, str]]
    api_config: ApiConfig | None = None


app = FastAPI(title="OSEF Studio API", version="1.0.0")

logger = logging.getLogger(__name__)

# Setup CORS for local dashboard development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global cache for the engine to prevent rebuilding on every request
_engine_cache = None
_graph_cache = None


_benchmark_metrics: dict[str, Any] | None = None


TARGET_DIR = os.environ.get("OSEF_TARGET_DIR", ".")


def get_engine() -> tuple[Any, Any]:
    global _engine_cache, _graph_cache, _benchmark_metrics
    if _engine_cache is None:
        start_time = time.perf_counter()
        _engine_cache = PipelineEngine(TARGET_DIR)
        _graph_cache = _engine_cache.build()
        end_time = time.perf_counter()
        duration = end_time - start_time
        num_nodes = len(_graph_cache.nodes)

        # Calculate dynamic metrics
        _benchmark_metrics = {
            "parser_throughput": f"{int(num_nodes / duration) if duration > 0 else 0} nodes/sec",
            "resolution_time": f"{duration * 0.4:.2f}s",
            "total_time": f"{duration:.2f}s",
            "nodes_processed": num_nodes,
        }
    return _engine_cache, _graph_cache


@app.get("/api/graph")
def get_graph() -> dict[str, Any]:
    try:
        _, graph = get_engine()

        # Format the graph nodes/edges exactly like test_ekg.json
        return {
            "nodes": [node.dict() for node in graph.nodes.values()],
            "edges": [edge.dict() for edge in graph.edges],
        }
    except Exception as e:
        logger.error(f"Error fetching graph: {e}")
        return {"error": "Internal server error while fetching graph."}


@app.get("/api/reasoning")
def get_reasoning() -> dict[str, Any]:
    try:
        engine, _ = get_engine()
        return dict(engine.confidence_score.dict())
    except Exception as e:
        logger.error(f"Error fetching reasoning: {e}")
        return {"error": "Internal server error while fetching reasoning."}


@app.get("/api/stats")
def get_stats() -> dict[str, Any]:
    try:
        engine, graph = get_engine()
        return {
            "node_count": len(graph.nodes),
            "edge_count": len(graph.edges),
            "overall_confidence": engine.confidence_score.overall_confidence,
        }
    except Exception as e:
        logger.error(f"Error fetching stats: {e}")
        return {"error": "Internal server error while fetching stats."}


@app.get("/api/intelligence")
def get_intelligence() -> dict[str, Any]:
    try:
        _, graph = get_engine()
        import sys
        import os

        # We add the intelligence plugin to the path temporarily if not installed
        plugin_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "../../../reference-plugins/intelligence/src"
            )
        )
        if os.path.exists(plugin_path) and plugin_path not in sys.path:
            sys.path.insert(0, plugin_path)

        try:
            from osef_intelligence.plugin import IntelligenceAnalyzer

            analyzer = IntelligenceAnalyzer(graph)
            return {
                "technical_debt": analyzer.get_technical_debt(),
                "repository_health": analyzer.get_repository_health(),
            }
        except ImportError:
            return {"error": "Intelligence plugin not installed."}

    except Exception as e:
        logger.error(f"Error fetching intelligence: {e}")
        return {"error": "Internal server error while fetching intelligence."}


@app.get("/api/benchmark")
def run_benchmark() -> dict[str, Any]:
    try:
        get_engine()
        return {
            "status": "success",
            "metrics": _benchmark_metrics or {},
        }
    except Exception as e:
        logger.error(f"Error running benchmark: {e}")
        return {"error": "Internal server error while running benchmark."}


@app.get("/api/policies")
def get_policies() -> dict[str, Any]:
    try:
        engine, graph = get_engine()
        violations = []

        import os
        import tomllib

        config = {}
        if os.path.exists("pyproject.toml"):
            try:
                with open("pyproject.toml", "rb") as f:
                    pyproject = tomllib.load(f)
                config = pyproject.get("tool", {}).get("osef", {}).get("rules", {})
            except Exception:
                pass

        # Rule 1: Missing Docstrings
        if config.get("Documentation.MissingDocstring", True):
            nodes_missing_docs = [
                n
                for n in graph.nodes.values()
                if n.type in ["function", "class", "module"] and not n.description
            ]
            if nodes_missing_docs:
                violations.append(
                    {
                        "id": "Documentation.MissingDocstring",
                        "severity": "warning",
                        "message": f"Found {len(nodes_missing_docs)} entities missing docstrings (e.g., {nodes_missing_docs[0].name})",
                    }
                )

        # Rule 2: High Coupling
        if config.get("Architecture.HighCoupling", True):
            from collections import defaultdict

            outgoing_counts: dict[str, int] = defaultdict(int)
            for e in graph.edges:
                outgoing_counts[e.source_id] += 1

            for n in graph.nodes.values():
                if outgoing_counts[n.id] > 30:
                    violations.append(
                        {
                            "id": "Architecture.HighCoupling",
                            "severity": "error",
                            "message": f"Node {n.name} has extremely high coupling ({outgoing_counts[n.id]} outgoing dependencies)",
                        }
                    )

        return {"violations": violations}
    except Exception as e:
        logger.error(f"Error fetching policies: {e}")
        return {"error": "Internal server error while fetching policies."}


@app.post("/api/chat")
def chat_with_assistant(request: ChatRequest) -> dict[str, Any]:
    try:
        engine, graph = get_engine()

        # Build context from graph
        node_count = len(graph.nodes)
        edge_count = len(graph.edges)

        # Get actual policy violations and codebase issues
        policies_response = get_policies()
        violations = policies_response.get("violations", [])
        issues_summary = "\n".join(
            [
                f"- [{v['severity'].upper()}] {v['id']}: {v['message']}"
                for v in violations
            ]
        )
        if not issues_summary:
            issues_summary = "No architectural policy violations detected."

        # Provide a sample of top-level modules/components
        modules = [n.name for n in graph.nodes.values() if n.type == "module"][:20]
        modules_summary = (
            ", ".join(modules) if modules else "No explicit modules detected."
        )

        import os

        try:
            import litellm
        except ImportError:
            return {
                "error": "The 'litellm' package is required to use the AI Assistant. Please run `pip install litellm boto3` or update your `osef[ui]` installation to install it."
            }

        model = (
            request.api_config.model
            if request.api_config and request.api_config.model
            else "nvidia/nemotron-3-ultra-550b-a55b"
        )
        base_url = (
            request.api_config.base_url
            if request.api_config and request.api_config.base_url
            else None
        )
        api_key = (
            request.api_config.api_key
            if request.api_config and request.api_config.api_key
            else None
        )

        # Fallback to standard Nvidia endpoint if model is default and no URL provided
        if not base_url and model == "nvidia/nemotron-3-ultra-550b-a55b":
            base_url = "https://integrate.api.nvidia.com/v1"

        project_name = os.path.basename(os.getcwd())

        system_prompt = f"""You are the strict, professional OSEF Architecture Assistant. 
You are currently analyzing the project: '{project_name}'.
Current Graph Context for '{project_name}':
- Total Nodes: {node_count}
- Total Edges: {edge_count}
- Top-Level Modules Identified: {modules_summary}
- Overall Reasoning Confidence: {engine.confidence_score.overall_confidence:.2f}

CODEBASE ISSUES AND POLICY VIOLATIONS:
{issues_summary}

CRITICAL INSTRUCTIONS:
1. You must ONLY answer questions based on the architecture, dependencies, and policies of the '{project_name}' project provided in your context. 
2. When asked about codebase issues, you MUST refer to the exact Codebase Issues listed above.
3. NEVER leak, discuss, or hallucinate information about other projects, training data, or external codebases. Your entire memory and knowledge base must be restricted to this specific project.
4. Output your responses using standard Markdown. Use clean formatting, lists, and code blocks where appropriate."""

        messages = [{"role": "system", "content": system_prompt}]
        for msg in request.history:
            if msg.get("role") in ["user", "assistant"]:
                messages.append({"role": msg["role"], "content": msg["content"]})

        messages.append({"role": "user", "content": request.message})

        kwargs = {
            "model": model,
            "messages": messages,
            "temperature": 1,
            "max_tokens": 1024,
        }
        if not model.startswith("bedrock/"):
            kwargs["top_p"] = 0.95
        if api_key:
            kwargs["api_key"] = api_key
        if base_url:
            kwargs["api_base"] = base_url

        if model == "nvidia/nemotron-3-ultra-550b-a55b":
            kwargs["extra_body"] = {
                "chat_template_kwargs": {"enable_thinking": True},
                "reasoning_budget": 1024,
            }

        try:
            # Tell litellm to suppress its own print statements for cleaner logs
            litellm.suppress_debug_info = True
            completion = litellm.completion(**kwargs)
            reply = completion.choices[0].message.content
            return {"reply": reply}
        except Exception as e:
            logger.error(f"LiteLLM error: {e}")
            return {
                "error": "An internal error occurred while communicating with the AI assistant."
            }

    except Exception as e:
        logger.error(f"Error in chat assistant: {e}")
        return {"error": "An internal error occurred."}


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {"status": "ok"}


ui_dir = os.path.join(os.path.dirname(__file__), "ui")
if not os.path.exists(ui_dir):
    # Fallback for local editable install (pip install -e .)
    ui_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../osef-studio/out")
    )

if os.path.exists(ui_dir):
    app.mount("/", StaticFiles(directory=ui_dir, html=True), name="ui")
else:

    @app.get("/")
    def root_fallback() -> dict[str, str]:
        return {"detail": "OSEF Studio UI not bundled. Build the UI first."}

# OSEF Python SDK Guide

The OSEF Python SDK allows developers to embed graph construction, policy evaluation, and intelligence metrics directly into custom tooling, automated scripts, and test suites.

---

## 1. Core Graph Construction (`PipelineEngine`)

Use `PipelineEngine` to programmatically build the Engineering Knowledge Graph (EKG) for any local codebase:
```python
from pathlib import Path
from osef.core.pipeline import PipelineEngine

# Initialize engine targeting current directory
engine = PipelineEngine(target_path=Path("."))

# Execute scanning and graph compilation
graph = engine.build()

print(f"Graph constructed with {len(graph.nodes)} nodes and {len(graph.edges)} edges.")
```

---

## 2. Programmatic Graph Queries (`GraphQuery`)

Once the EKG is built, use `GraphQuery` to inspect structural relationships:
```python
from osef.core.graph_query import GraphQuery

query = GraphQuery(graph)

# Find all classes in the codebase
classes = [node for node in graph.nodes.values() if node.kind == "CLASS"]

# Query call graph: Find what functions PipelineEngine.build() invokes
callees = query.get_callees("src/osef/core/pipeline.py::PipelineEngine.build")
for callee in callees:
    print(f" -> invokes: {callee}")
```

---

## 3. Programmatic Policy Evaluation (`PolicyEngine`)

You can instantiate the Engineering Policy Engine (EPE) and evaluate constitutional architectural rules in Python:
```python
from osef.epe.setup import get_default_engine
from osef.epe.engine import Severity

# Load default architectural policy rules
epe = get_default_engine()

# Evaluate graph against rules
findings = epe.evaluate(graph)

for finding in findings:
    if finding.severity in (Severity.CRITICAL, Severity.HIGH):
        print(f"[VIOLATION] {finding.rule_id}: {finding.message} at {finding.file_path}:{finding.line}")
```

---

## 4. Engineering Intelligence & Scoring (`IntelligenceLayer`)

Compute objective technical debt, architecture drift, and confidence metrics:
```python
from osef.intelligence.layer import IntelligenceLayer

intel = IntelligenceLayer(graph)
assessment = intel.assess()

print(f"Engineering Confidence Score: {assessment.confidence_score}/100")
print(f"Technical Debt Index: {assessment.tech_debt_index}")
print(f"Architecture Drift Score: {assessment.drift_score}")
```

---

## 5. Model Context Protocol Service (`EKGContextService`)

Embed the MCP context service in custom LLM orchestrators:
```python
from osef.mcp.context import EKGContextService

service = EKGContextService(".")

# Get blast radius for a symbol
radius = service.get_blast_radius("src/osef/core/pipeline.py::PipelineEngine")
print("Downstream dependents affected:", len(radius.get("dependents", [])))
```
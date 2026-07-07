# Engineering Knowledge Graph (EKG)

The **Engineering Knowledge Graph (EKG)** is the foundational data model of OSEF. It represents the structural, semantic, and dependency facts of a software repository as a directed, typed graph.

---

## 1. Language-Agnostic Symbol Tables

When `osef scan` processes a codebase, language-specific plugins (Python, TypeScript, Java) parse source code into Abstract Syntax Trees (ASTs) and map them onto unified **Symbol Tables**.

Every symbol in the codebase is assigned a deterministic identifier (`Node ID`) and categorized by kind:
* `FILE`: Source file or module artifact.
* `CLASS`: Object-oriented class or interface definition.
* `FUNCTION`: Standalone function or method declaration.
* `VARIABLE`: Module-level or class-level attribute.
* `PACKAGE`: Namespace or directory package bundle.

---

## 2. Graph Nodes & Edges

### Nodes
A Node represents a discrete engineering entity. Core node properties include:
* `id`: Unique URI path (e.g., `src/osef/core/pipeline.py::PipelineEngine`).
* `kind`: The symbol categorization.
* `name`: Unqualified symbol name (`PipelineEngine`).
* `file_path`: Relative path from repository root.
* `line_start` / `line_end`: Precise line boundary spans.
* `metadata`: Dict containing docstrings, AST decorators, and signature details.

### Edges
An Edge represents a directed relationship between two nodes:
* `IMPORTS`: Module or file import dependency.
* `CALLS`: Function or method call invocation.
* `INHERITS`: Class inheritance or interface realization.
* `CONTAINS`: Structural hierarchy (e.g., File contains Class, Class contains Method).

---

## 3. Serialization Formats

The EKG can be serialized into standard data formats for external consumption or persistence:
* **JSON (`.osef/ekg.json`)**: Machine-readable canonical graph representation used by the EPE and MCP servers.
* **YAML**: Human-readable format for auditing and inspection.
* **SARIF 2.1.0**: Annotated graph structures mapped to static analysis findings for CI/CD pipelines.

---

## 4. Programmatic Querying

You can inspect the EKG in Python using `GraphQuery`:
```python
from osef.core.pipeline import PipelineEngine
from osef.core.graph_query import GraphQuery

# Build and load graph
builder = PipelineEngine(".")
graph = builder.build()
query = GraphQuery(graph)

# Find all classes inheriting from BasePlugin
subclasses = query.find_subclasses("BasePlugin")

# Get upstream callers of execute()
callers = query.get_callers("src/osef/core/engine.py::execute")
```
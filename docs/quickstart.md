# OSEF Quick Start Guide

This step-by-step guide walks you through scanning a repository, building a deterministic Engineering Knowledge Graph (EKG), evaluating constitutional policies, and launching the Model Context Protocol (MCP) server.

---

## 1. Verify Environment Readiness

Run `doctor` to confirm that the Python runtime, language parsers, and AST extractors are configured properly:
```bash
osef doctor
```

---

## 2. Scan Codebase & Build EKG

Execute `scan` against your repository root. OSEF dynamically invokes language plugins (Python, TypeScript, Java) to parse source code, extract Symbol Tables, and construct semantic facts:
```bash
osef scan . --format json --output .osef/
```

This generates:
* `.osef/ekg.json`: The complete, deterministic cross-domain graph.
* `.osef/symbols/`: Language-agnostic symbol tables.

---

## 3. Validate Graph Integrity

Run `validate` to verify topological consistency, check for dangling edge references, and assert structural invariants:
```bash
osef validate repository .
```

---

## 4. Evaluate Architectural Policies (EPE)

Run the declarative Engineering Policy Engine against the EKG to detect architecture drift, cyclic dependencies, missing documentation, and boundary violations:
```bash
# Terminal rich table summary
osef policy check .

# Generate standard SARIF 2.1.0 output for CI/CD pipelines
osef policy check . --format sarif --output report.sarif --ci
```

---

## 5. Launch Model Context Protocol (MCP) Server

To expose the EKG directly to AI coding assistants (VS Code, Antigravity IDE, Claude), start the standard `stdio` MCP server:
```bash
osef mcp serve .
```

The server exposes 5 semantic tools:
* `blast_radius`: Analyze downstream impact of modifying a symbol.
* `dependency_path`: Discover shortest import/call path between nodes.
* `policy_violations`: Query active EPE policy findings.
* `architecture_summary`: Retrieve high-level repository intelligence.
* `symbol_info`: Lookup AST symbol definition details.
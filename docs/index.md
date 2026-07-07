# Open Source Engineering Framework (OSEF)

**OSEF** is an immutable, deterministic **Engineering Knowledge Graph (EKG)** and declarative **Engineering Policy Engine (EPE)** designed to provide cross-language structural analysis, architectural governance, and AI-native semantic context injection.

---

## Architectural Principles & Core Differentiation

* **Not an AST Linter or Naive RAG**: Unlike conventional syntax checkers (ESLint, Ruff) or simple text-based LLM retrieval wrappers, OSEF transforms source code across diverse languages (Python, TypeScript, Java) into unified, language-agnostic **Symbol Tables** and deterministic semantic facts.
* **The Semantic Moat**: By representing codebase structure, dependency hierarchies, call graphs, and architectural boundaries as a formal graph, OSEF eliminates hallucination in AI agents and enables mathematically verifiable policy enforcement.
* **Open Industry Standards**: All policy evaluations, graph queries, and pipeline outputs conform to standardized interchange protocols including **SARIF 2.1.0** (Static Analysis Results Interchange Format), **JUnit XML**, and the **Model Context Protocol (MCP)**.

---

## Key Capabilities

1. **Deterministic EKG Construction**: Multi-language AST parsing that extracts definitions, references, inheritance trees, and call relationships into an immutable structural graph.
2. **Declarative Engineering Policy Engine (EPE)**: Execute constitutional architecture rules (e.g., layer isolation, dependency directionality, docstring completeness) with zero false positives.
3. **Model Context Protocol (MCP) Server**: Expose `blast_radius`, `dependency_path`, and `symbol_info` tools over standard I/O (`stdio`) directly to LLM assistants (VS Code, Antigravity IDE, Claude).
4. **Universal Distribution**: Run locally via PyPI wheels, execute reproducibly via Docker OCI containers, or automate within CI/CD pipelines using GitHub Actions (`action.yml`).
5. **Community Marketplace & Benchmark Leaderboard**: Package, cryptographically sign (Ed25519), and verify language plugins, or compute objective engineering confidence metrics across repositories.

---

## Next Steps

* **[Installation Guide](installation.md)**: Set up OSEF locally, via Docker, or in VS Code.
* **[Quick Start](quickstart.md)**: Build your first EKG and run policy evaluations.
* **[CLI Reference](cli_reference.md)**: Complete command-line option documentation.
* **[Architecture Overview](architecture.md)**: Dive into the EKG graph schema and EPE specifications.
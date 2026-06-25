# OSEF MVP Boundary

## Objective
To protect implementation focus by explicitly defining what is required for OSEF `v1.0.0` and explicitly excluding out-of-scope ideas.

## IN SCOPE (Required for v1.0.0)
The MVP must deliver a functional, local-first engineering operating system.

- **Core Runtime:** Dependency Injection, Async Event Bus.
- **Knowledge System:** Markdown Knowledge Provider, local EKK storage.
- **Extensibility:** Local Plugin Runtime and Discovery.
- **Interfaces:** Python SDK (`osef.init()`), Typer CLI.
- **OSTE MVP:** Repository Analyzer (AST parsing), Documentation Generator (Jinja2).
- **Workflows:** Interactive repair for standard governance files.
- **Certification:** Baseline Certification Engine producing a terminal score.
- **Templates:** GitHub Repository Templates for playbooks.
- **Packaging:** Standard Python publishing (`uv` support).

## OUT OF SCOPE (Explicitly Excluded from v1.0.0)
If an implementation task maps to any of the following, it MUST be deferred.

- **Distributed Systems:** Distributed Runtime, Remote Execution, Cloud Synchronization.
- **Advanced Databases:** Graph Databases, Vector Databases, Local LLM Embeddings.
- **Ecosystem:** Plugin Marketplace, Package Registry integration (beyond standard PyPI).
- **Collaboration:** Team Workspaces, Enterprise Features, Team Knowledge Spaces.
- **Agents:** Multi-Agent Runtime, GitHub Bot integration, autonomous PR generation.
- **Integrations:** Personal Knowledge Management (Obsidian/Notion) sync.

These items belong in `v2.x` or the `IDEAS_PARKING_LOT.md`. The MVP must remain radically focused on local repository transformation.

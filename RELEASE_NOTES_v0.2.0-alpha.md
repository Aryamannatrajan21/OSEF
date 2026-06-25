# Release Notes: OSEF v0.2.0-alpha

## Engineering Foundation

This release marks the completion of **Sprint 1**. 

The OSEF architectural blueprint from `v0.1.0-alpha` has been fully transitioned into an operational software foundation. There is no domain logic or "AI" yet—this is strictly the production-grade plumbing required to scale.

### 🏗 What is included in this release?
- **Core Runtime**: Asynchronous Dependency Injection container and Bootstrapper.
- **Event Bus**: Extensible Publisher/Subscriber architecture for internal decoupling.
- **CLI Framework**: Robust Typer CLI with `init`, `validate`, and `docs` commands.
- **Engineering Knowledge Graph**: Pydantic models capturing the EKG schema (Nodes & Edges).
- **Plugin SDK**: Interfaces, Manifests, and Plugin Registry to enforce strict boundary separation.
- **Version Management**: Centralized PEP 440 versioning (`0.2.0a0`) dynamically loaded via `importlib.metadata`.

### Quality Metrics
- **Test Coverage**: 93%
- **Linting & Typing**: Zero errors (`ruff`, `mypy`).
- **Installability**: Strictly enforces Python 3.12+ for modern async and typing features.

### 🚀 What's Next?
**Sprint 2: The Transformation Engine** begins immediately. We will parse ASTs and build the first actual engineering rules.

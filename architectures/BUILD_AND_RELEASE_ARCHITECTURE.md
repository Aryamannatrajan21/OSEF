# OSEF Build & Release Architecture

## Overview
This document specifies how OSEF itself is built, tested, and released. It ensures the framework remains stable, cross-platform, and adheres to its own rigorous standards.

## 1. Versioning Strategy
OSEF strictly follows Semantic Versioning (SemVer) 2.0.0.
- **MAJOR:** Breaking changes to Public API (`contracts/`, `interfaces/`) or CLI syntax.
- **MINOR:** New backward-compatible features, core plugins, or EKK rulesets.
- **PATCH:** Bug fixes, performance improvements in internal implementations.

## 2. CI/CD Pipeline
The release pipeline is entirely automated using GitHub Actions.

### 2.1. Pull Request Validation
Every PR must pass:
1. **Linting:** `ruff check` and `ruff format --check`.
2. **Type Checking:** `mypy --strict src/`.
3. **Unit Tests:** `pytest tests/` (Coverage must remain > 90%).
4. **Architectural Validation:** A custom script ensuring no imports violate the `DEPENDENCY_GRAPH.md`.

### 2.2. Release Automation
Releases are triggered by GitHub Releases / Tags.
1. Tests pass on Ubuntu, macOS, and Windows.
2. `uv build` compiles the sdist and wheel.
3. `twine` publishes securely to PyPI via Trusted Publishing (OIDC).
4. Auto-generated release notes pull from the commit history and ADRs.

## 3. Dependency Pinning
- **Libraries (`src/`):** Dependencies in `pyproject.toml` are loosely pinned (e.g., `typer >= 0.9.0, < 1.0.0`) to maximize compatibility for users installing OSEF alongside other tools.
- **Development (`tests/`, CI):** `uv.lock` is committed to ensure fully deterministic and reproducible CI builds.

## 4. Documentation Release
The documentation website (generated from `docs/` and `architectures/`) is automatically built using MkDocs or Sphinx and deployed to GitHub Pages upon every release.

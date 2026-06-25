# OSEF Dependency Matrix

## Overview
This matrix explicitly defines which subsystems are allowed to depend on which other subsystems, translating the `DEPENDENCY_GRAPH.md` into concrete rules.

## Internal Dependencies (The "Allowed" Map)
| Module | May Import From | May NOT Import From |
|--------|-----------------|---------------------|
| `contracts` | `typing`, stdlib | *Anything else in OSEF* |
| `interfaces` | `contracts` | `services`, `adapters`, `core`, `cli` |
| `services` | `contracts`, `interfaces` | `adapters`, `core`, `cli` |
| `adapters` | `contracts`, `interfaces` | `services`, `core`, `cli` |
| `core` | `contracts`, `services`, `adapters` | `cli` |
| `cli` | `core`, `contracts` | `services`, `adapters` |

## External Package Dependencies (The "Budget")
| Package | Version | Purpose |
|---------|---------|---------|
| `typer` | `>= 0.9.0` | CLI generation and arguments parsing |
| `pydantic` | `>= 2.0.0` | Strict Domain Model validation |
| `pydantic-settings` | `>= 2.0.0` | `.env` and configuration resolution |
| `jinja2` | `>= 3.0.0` | Templating generated artifacts (e.g., ADRs) |

## Test-Only Dependencies
| Package | Purpose |
|---------|---------|
| `pytest` | Test execution |
| `pytest-asyncio` | Async test execution |
| `pytest-syrupy` | CLI snapshot testing |
| `ruff` | Linting and formatting |
| `mypy` | Static type analysis |

## Enforcement
These rules will be enforced via a custom Python script or `import-linter` configured in `pyproject.toml` that runs on every Pull Request.

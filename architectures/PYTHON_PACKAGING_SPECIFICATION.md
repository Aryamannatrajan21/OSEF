# OSEF Python Packaging Specification

## Overview
Following the **Minimal Core, Extensible Edge** philosophy, this document specifies the exact dependencies and packaging tools used to build OSEF.

## 1. Toolchain
- **Python Version:** `3.13+`
- **Package Manager:** `uv` (Fast, deterministic dependency resolution)
- **Build Backend:** `hatchling` (Standard, highly extensible PEP 517 backend)

## 2. Core Dependencies
The MVP Core will rely **exclusively** on the following external packages to minimize startup latency, security surface, and installation size:
1. **`typer`**: For CLI generation and rich terminal output.
2. **`pydantic`**: For strict domain model validation (Events, Knowledge Items).
3. **`pydantic-settings`**: For type-safe configuration loading from environment variables and `.env` files.
4. **`jinja2`**: For templating Prompts and generated Artifacts.

## 3. Storage Layer
- **MVP Default:** `sqlite3` (Python Standard Library). No ORM is used in the core.
- **File System:** `pathlib` (Python Standard Library).

## 4. Development Dependencies
Used only in CI and local development environments:
- `pytest`, `pytest-asyncio` (Testing)
- `ruff` (Linting and Formatting)
- `mypy` (Static Type Checking)

## 5. Plugin Distribution
Third-party or optional capabilities will be distributed as separate PyPI packages (e.g., `pip install osef-openai`).

Plugins declare OSEF as a dependency:
```toml
[project]
name = "osef-openai"
dependencies = [
    "osef >= 1.0.0"
]
```

## 6. Project Configuration (`pyproject.toml` template)
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "osef"
version = "0.1.0"
description = "The universal standardization layer for open source."
requires-python = ">=3.13"
dependencies = [
    "typer>=0.9.0",
    "pydantic>=2.0.0",
    "pydantic-settings>=2.0.0",
    "jinja2>=3.0.0"
]

[project.scripts]
osef = "osef.cli.main:app"
```

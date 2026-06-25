# OSEF Package Architecture

## Overview
This specification defines the structural layout of the `osef` Python package source tree (`src/osef/`). It enforces the boundaries established in the Dependency Graph.

## Directory Structure

```text
osef/
├── src/
│   └── osef/
│       ├── __init__.py           # Facade exposing osef.init() and SDK
│       │
│       ├── contracts/            # LAYER 1: No internal imports allowed
│       │   ├── events.py         # Base Event models
│       │   ├── models.py         # Pydantic/Dataclass domain models
│       │   └── providers.py      # typing.Protocol interfaces
│       │
│       ├── interfaces/           # LAYER 2: ABCs for extension
│       │   ├── plugin.py         # BasePlugin
│       │   └── storage.py        # BaseStorageAdapter
│       │
│       ├── core/                 # LAYER 4: Wiring and Orchestration
│       │   ├── container.py      # Dependency Injection Container
│       │   ├── bootstrapper.py   # Initialization logic
│       │   └── context.py        # Project context resolution
│       │
│       ├── services/             # LAYER 3: Core Logic (OSTE, EventBus)
│       │   ├── engine.py         # Transformation Engine orchestration
│       │   ├── events.py         # EventBusProvider implementation
│       │   └── knowledge.py      # EKK Service implementation
│       │
│       ├── adapters/             # LAYER 3: Concrete IO
│       │   ├── sqlite.py         # SQLite Knowledge storage
│       │   ├── markdown.py       # File system parser
│       │   └── git.py            # Local Git CLI wrapper
│       │
│       └── cli/                  # LAYER 5: Presentation
│           ├── main.py           # Typer application
│           ├── commands/         # Individual osef subcommands
│           └── output/           # Rich formatting and tables
│
├── tests/                        # Mirrors src/ structure
├── pyproject.toml                # Defined by the Packaging Spec
└── README.md
```

## Ownership Rules
- `contracts/` and `interfaces/` are the **Public API**. Breaking changes here require a major version bump.
- `services/` and `adapters/` are the **Internal API**. External plugins attempting to import from these directories do so at their own risk.
- The `cli/` module contains zero business logic. It translates CLI arguments into `models.py` instances and invokes `core/`.

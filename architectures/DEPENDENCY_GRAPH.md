# OSEF Dependency Graph

## Overview
This document maps the allowed dependencies between internal OSEF subsystems to strictly prevent circular imports and guarantee architectural layering.

## 1. Architectural Layers

### Layer 1: Contracts (Bottom)
Contains `typing.Protocol`, Dataclasses, and Exceptions.
- **Allowed to import:** `typing`, `dataclasses`, Python Standard Library.
- **Cannot import from:** Any other OSEF module.

### Layer 2: Interfaces
Contains ABCs (`BasePlugin`, `BaseStorageAdapter`).
- **Allowed to import:** `contracts`.
- **Cannot import from:** `core`, `services`, `adapters`.

### Layer 3: Services & Adapters
Contains concrete implementations (`SqliteStorageAdapter`, `EventBus`).
- **Allowed to import:** `contracts`, `interfaces`.
- **Cannot import from:** `core`, CLI, other services (must use DI).

### Layer 4: Core (Dependency Injector)
Contains the bootstrapper and DI wiring.
- **Allowed to import:** `contracts`, `services`, `adapters`.
- **Cannot import from:** `cli`.

### Layer 5: CLI & SDK (Top)
User-facing entry points.
- **Allowed to import:** `core`, `contracts`.
- **Cannot import from:** `services`, `adapters` directly.

## 2. Visual Dependency Map

```mermaid
graph TD
    %% Define Nodes
    CLI[CLI (Typer)]
    SDK[Public SDK]
    CORE[Core / Bootstrapper]
    OSTE[Transformation Engine]
    EKK_IMPL[Knowledge Service]
    EVENT_IMPL[Event Bus Service]
    ADAPTERS[Storage Adapters]
    INTERFACES[Interfaces / ABCs]
    CONTRACTS[Contracts / Protocols]

    %% Layer 5 to Layer 4
    CLI --> CORE
    SDK --> CORE
    CLI --> CONTRACTS
    SDK --> CONTRACTS

    %% Layer 4 to Layer 3
    CORE --> OSTE
    CORE --> EKK_IMPL
    CORE --> EVENT_IMPL
    CORE --> ADAPTERS

    %% Layer 3 to Layer 1 & 2
    OSTE --> CONTRACTS
    EKK_IMPL --> CONTRACTS
    EVENT_IMPL --> CONTRACTS
    ADAPTERS --> INTERFACES
    ADAPTERS --> CONTRACTS
    OSTE --> INTERFACES

    %% Layer 2 to Layer 1
    INTERFACES --> CONTRACTS
```

## 3. Enforcement
- Imports from `services` to `core` or `cli` are strictly forbidden and will result in CI failure.
- `ruff` or `import-linter` must be configured to assert these boundary rules.

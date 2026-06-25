# OSEF Internal API Specification

## Overview
The Internal API encompasses the actual implementations, orchestration logic, and CLI mapping. It is **not** covered by Semantic Versioning guarantees. Plugins importing from these modules will break.

## 1. Import Boundaries
The Internal API is confined to:
- `osef.services.*`
- `osef.adapters.*`
- `osef.core.*` (excluding `context`)
- `osef.cli.*`

## 2. The Dependency Injector (`osef.core.container`)
Manages the lifecycle and resolution of singletons.
- `class CoreContainer:`
  - `def register(protocol: type, implementation: Any)`
  - `def resolve(protocol: type) -> Any`

## 3. Core Services (`osef.services.*`)
Concrete implementations of the Public Protocols.
- `EventBus`: Implements `EventBusProvider` using `asyncio.Queue` and background task workers.
- `KnowledgeRouter`: Implements `KnowledgeProvider`, routing requests to the appropriate `StorageAdapter`.
- `TransformationEngine`: The OSTE orchestration logic that coordinates `osef analyze` and `osef certify`.

## 4. Adapters (`osef.adapters.*`)
Concrete IO wrappers.
- `SqliteKnowledgeAdapter`: Reads EKK rules from an internal `.sqlite` file or JSON/Markdown dump.
- `LocalFileStorage`: Implements `StorageProvider` using Python's `pathlib` and `aiofiles`.

## 5. CLI Presentation (`osef.cli.*`)
Built entirely on `Typer`.
- Contains no business logic.
- Parses command line flags into `ProjectConfig` instances.
- Calls `await osef.init()` to retrieve the DI container.
- Invokes methods on the `TransformationEngine`.
- Formats `CertificationScore` dataclasses into rich terminal output using the `rich` library (bundled with Typer).

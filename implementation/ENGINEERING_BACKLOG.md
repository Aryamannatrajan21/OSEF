# OSEF Engineering Backlog

This backlog maps implementation tasks to the established architecture. Sprints 1-3 are fully detailed. Sprints 4-10 are defined as progressive epics.

---

## Sprint 1: Core Runtime Basics

### TASK-001: Scaffolding `src/osef/`
- **Description:** Initialize the package structure according to `PACKAGE_ARCHITECTURE.md`.
- **Priority:** Critical
- **Complexity:** Low
- **Dependencies:** None
- **Related Arch:** `PACKAGE_ARCHITECTURE.md`, `PYTHON_PACKAGING_SPECIFICATION.md`
- **Acceptance Criteria:** `uv build` successfully creates a wheel. `ruff` and `mypy` pass on empty init files.

### TASK-002: Implement Service Protocols
- **Description:** Define `typing.Protocol` classes for `EventBusProvider`, `KnowledgeProvider`, `StorageProvider` in `contracts/providers.py`.
- **Priority:** Critical
- **Complexity:** Low
- **Related Arch:** `SERVICE_CONTRACTS.md`
- **Acceptance Criteria:** Protocols defined with no concrete logic. Type checking passes.

### TASK-003: Implement Domain Models
- **Description:** Implement `ProjectContext` and `Event` base models using Pydantic.
- **Priority:** High
- **Complexity:** Low
- **Related Arch:** `DOMAIN_MODELS.md`
- **Acceptance Criteria:** Models enforce immutability (`frozen=True`).

### TASK-004: Implement Dependency Injector
- **Description:** Build the `CoreContainer` in `core/container.py` capable of registering and resolving protocols to implementations.
- **Priority:** Critical
- **Complexity:** Medium
- **Acceptance Criteria:** Unit tests prove singletons resolve correctly. `CircularDependencyError` is thrown if detected.

### TASK-005: Implement Async Event Bus
- **Description:** Build the concrete `EventBus` in `services/events.py` using `asyncio.Queue`.
- **Priority:** High
- **Complexity:** High
- **Related Arch:** `EVENT_ARCHITECTURE.md`
- **Acceptance Criteria:** Integration test proves 100 concurrent events are routed to 3 subscribers without dropping.

---

## Sprint 2: Knowledge Layer (EKK)

### TASK-006: Markdown Storage Adapter
- **Description:** Implement `LocalFileStorage` adhering to `StorageProvider` using `aiofiles`.
- **Priority:** High
- **Complexity:** Medium
- **Acceptance Criteria:** Can asynchronously read and write to local disk.

### TASK-007: SQLite Knowledge Adapter
- **Description:** Implement `SqliteKnowledgeAdapter` using `sqlite3` to cache EKK rules parsed from Markdown.
- **Priority:** High
- **Complexity:** High
- **Related Arch:** `EKK_ARCHITECTURE.md`
- **Acceptance Criteria:** Database initialized. Can query by tags.

---

## Sprint 3: Plugin Ecosystem

### TASK-008: Plugin Base Classes
- **Description:** Implement `BasePlugin` ABC in `interfaces/plugin.py`.
- **Priority:** High
- **Complexity:** Low
- **Related Arch:** `PUBLIC_API_SPECIFICATION.md`
- **Acceptance Criteria:** Requires `register_hooks` method implementation.

### TASK-009: Plugin Discovery Mechanism
- **Description:** Implement `PluginManager` that scans `importlib.metadata.entry_points` for `osef.plugins`.
- **Priority:** High
- **Complexity:** Medium
- **Acceptance Criteria:** Can dynamically load a dummy plugin at boot time.

---

## Progressive Epics (Sprints 4-10)

- **EPIC-SPRINT-04:** Implement the SDK Facade (`osef.init()`).
- **EPIC-SPRINT-05:** Implement the CLI via Typer (`osef analyze`, `osef init`).
- **EPIC-SPRINT-06:** Implement `TransformationEngine` (OSTE) static analysis.
- **EPIC-SPRINT-07:** Connect OSTE AST outputs to EKK Validation logic.
- **EPIC-SPRINT-08:** Implement interactive repair and Jinja2 artifact generation.
- **EPIC-SPRINT-09:** Implement Open Source Certification algorithms.
- **EPIC-SPRINT-10:** Execute release strategy and documentation deployments.

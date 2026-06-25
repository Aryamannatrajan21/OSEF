# OSEF Testing Strategy

Testing must validate the architecture, not just code execution.

## 1. Unit Tests (`tests/unit/`)
- Validate isolated logic (e.g., parsing a specific markdown string).
- **Rule:** Storage and Event Bus must be mocked using standard `unittest.mock` or internal `TestCore` classes. No disk I/O is allowed.

## 2. Integration Tests (`tests/integration/`)
- Validate the interaction between multiple services (e.g., Engine -> EventBus -> SqliteAdapter).
- **Rule:** Uses temporary in-memory SQLite databases and `tempfile` directories.

## 3. CLI Snapshot Tests (`tests/cli/`)
- Validate the Developer Experience.
- **Rule:** Uses `pytest-syrupy` or similar to take snapshots of the exact terminal output (including colors/formatting). If the CLI `--help` text changes unexpectedly, the test fails.

## 4. Architecture Conformance Tests (`tests/arch/`)
- Validate `DEPENDENCY_GRAPH.md`.
- **Rule:** A script parses the `src/` ASTs to ensure `contracts/` never imports from `services/`.

## 5. Plugin Compatibility Tests
- Validate Public API stability.
- **Rule:** A suite that loads a mock V1 plugin and ensures current Core updates do not break `register_hooks` or standard Event signatures.

## 6. Golden File Tests
- Used for `osef repair` outputs.
- **Rule:** Provide a broken repository state as an input fixture. Run `osef repair`. Compare the mutated files against a "Golden" perfectly formatted fixture directory.

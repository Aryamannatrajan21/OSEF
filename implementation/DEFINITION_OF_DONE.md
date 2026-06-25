# OSEF Definition of Done (DoD)

Before any Implementation Task or Pull Request can be merged into `main`, it MUST satisfy the following criteria:

## 1. Architectural Alignment
- [ ] The implementation strictly mirrors the relevant Phase 0 architectural specification.
- [ ] If the implementation requires deviating from the architecture, an **ADR** (Architectural Decision Record) must be created and approved first.

## 2. Code Quality
- [ ] Strict type checking passes: `mypy --strict src/` returns 0 errors.
- [ ] Linting and formatting passes: `ruff check` and `ruff format --check`.
- [ ] No circular dependencies were introduced (enforced via `import-linter` or script).
- [ ] The Dependency Budget was respected (no unauthorized third-party `pip` dependencies added to the Core).

## 3. Testing
- [ ] Unit tests are written for all new logic.
- [ ] Integration tests verify interactions across the Event Bus.
- [ ] Overall line coverage remains > 90%.

## 4. Documentation
- [ ] Public methods and classes have Google-style docstrings.
- [ ] `docs/` or `playbooks/` are updated if user-facing behavior changed.

## 5. Developer Experience (DX)
- [ ] CLI commands follow the `COMMAND_DESIGN_GUIDELINES.md`.
- [ ] Errors raised use the Tripartite structure (What, Why, Fix) from `ERROR_RECOVERY_GUIDELINES.md`.
- [ ] The feature passes the `DX_CHECKLIST.md`.

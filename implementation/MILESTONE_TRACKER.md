# OSEF Milestone Tracker

This document defines the high-level milestones from Phase 0 to `v1.0`.

## Milestone 0: Architecture Complete (DONE)
- [x] Founder Manifesto
- [x] Constitution
- [x] Governance and DX Specifications
- [x] Architecture Review Passed
- [x] Implementation Plan Approved

## Milestone 1: Runtime MVP (Target: Sprint 3)
- [ ] Dependency Injector functions.
- [ ] Event Bus routes async messages.
- [ ] Basic Markdown storage can be queried.
- *Exit Criteria:* We can instantiate the `CoreContainer` and fire an event successfully without errors.

## Milestone 2: SDK & CLI Alpha (Target: Sprint 5)
- [ ] `osef.init()` exposes the Core API.
- [ ] `Typer` CLI is scaffolded with `--help`.
- [ ] `osef init` generates basic configuration.
- *Exit Criteria:* A user can `pip install` the alpha build and run `osef` in their terminal to see the help menu.

## Milestone 3: OSTE MVP (Target: Sprint 7)
- [ ] OSTE static analysis reads local files.
- [ ] Data maps to EKK rules.
- [ ] Interactive output formats correctly.
- *Exit Criteria:* `osef analyze` successfully warns a user about a missing `LICENSE` file based on a rule in the EKK.

## Milestone 4: Beta Release (Target: Sprint 9)
- [ ] `osef repair` generates artifacts.
- [ ] `osef certify` scores the repository.
- [ ] Plugin ecosystem is tested.
- *Exit Criteria:* Beta is published to PyPI. Community testing begins.

## Milestone 5: v1.0 Release Candidate (Target: Sprint 10)
- [ ] All P0 bugs resolved.
- [ ] Documentation fully synced.
- [ ] Multi-OS CI/CD pipelines green.
- *Exit Criteria:* `v1.0.0` is published and formally announced.

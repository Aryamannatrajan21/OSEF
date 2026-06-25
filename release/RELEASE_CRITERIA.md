# OSEF Release Criteria

This document defines the objective criteria required to advance through the pre-release stages to `v1.0.0`.

## Alpha Release Criteria
- **Architecture:** Core Runtime (DI, Event Bus) implemented.
- **Functionality:** `osef init` and basic `osef analyze` functioning for local Markdown.
- **Testing:** Unit test coverage > 80% for Core.
- **Packaging:** Published to PyPI as `osef==1.0.0-alpha.1`.

## Beta Release Criteria
- **Architecture:** Plugin Runtime implemented and tested with at least one external mock plugin.
- **Functionality:** OSTE MVP complete. `osef repair` interactive prompts functioning.
- **Testing:** Integration tests cover all primary Event Bus flows. CLI snapshot tests implemented. Line coverage > 90%.
- **Documentation:** `README.md`, Installation Guides, and Playbooks are accurate to the implementation.

## Release Candidate (RC) Criteria
- **Functionality:** Certification Engine complete. GitHub Action headless mode verified.
- **Performance:** `osef analyze` executes on a medium-sized repository (1,000 files) in under 5 seconds.
- **Testing:** Zero known `P0` or `P1` bugs. 
- **Validation:** Deployed successfully against 3 distinct external repositories (e.g., a Django app, a Typer CLI, a FastAPI service) confirming correct architectural analysis.

## v1.0.0 Stable Release Criteria
- **Stability:** RC has been public for 14 days without any `P0` bug reports.
- **Documentation:** `docs.osef.io` (or equivalent) deployed and publicly accessible.
- **Governance:** `CODE_OF_CONDUCT.md`, `SECURITY.md`, and `CONTRIBUTING.md` established on the OSEF repository itself.

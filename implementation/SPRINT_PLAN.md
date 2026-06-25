# OSEF Sprint Plan

Each sprint is designed to produce a working, independently testable increment. 

## Sprint 1: Core Runtime Basics
- **Focus:** Repository structure validation, Dependency Injection, Configuration, Logging, Event Bus.
- **Outcome:** The `osef` python package can be imported, and internal events can be fired and caught by the DI container.

## Sprint 2: Knowledge Layer (EKK)
- **Focus:** Engineering Knowledge Kernel interfaces, Storage abstraction, Markdown knowledge provider.
- **Outcome:** OSEF can query local markdown rules and return them as typed Pydantic models.

## Sprint 3: Plugin Ecosystem
- **Focus:** Plugin Runtime, Plugin Discovery, Plugin Registry.
- **Outcome:** Third-party plugins can register hooks with the Event Bus via Python entry points.

## Sprint 4: SDK Foundation
- **Focus:** Exposing `osef.contracts` and the `osef.init()` bootstrapper.
- **Outcome:** Python scripts can programmatically initialize OSEF and query the EKK without CLI usage.

## Sprint 5: CLI Foundation
- **Focus:** Typer integration, `--help` menus, Output formatting, Interactive prompts.
- **Outcome:** The `osef` command works in terminal, displays help, and can run `osef init` to generate configurations.

## Sprint 6: Repository Analysis
- **Focus:** OSTE Static Analysis, file parsing, AST extraction.
- **Outcome:** `osef analyze` can read a repository and identify missing standard files (e.g., `LICENSE`, `README.md`).

## Sprint 7: OSTE MVP
- **Focus:** Linking Analysis data to EKK rules.
- **Outcome:** `osef analyze` correctly warns the user about architectural violations based on their project profile.

## Sprint 8: Documentation Generation
- **Focus:** `osef repair` functionality, Jinja2 templating for ADRs and Governance files.
- **Outcome:** OSEF can automatically write missing governance files with user consent.

## Sprint 9: Certification Engine
- **Focus:** Scoring algorithms, Badge generation, CI/CD headless mode.
- **Outcome:** `osef certify` yields a deterministically reproducible open-source score.

## Sprint 10: Release Candidate
- **Focus:** Bug fixes, Performance optimization, PyPI publishing workflows.
- **Outcome:** `v1.0.0` published.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [0.2.0a0] - 2026-06-26

### Added
- **Engineering Foundation:** Implemented Sprint 1 Core Runtime, DI Container, and Async Event Bus.
- **CLI Framework:** Established Typer-based CLI for initialization and validation.
- **Knowledge Graph:** Pydantic models for the Engineering Knowledge Graph (EKG).
- **Version Management:** Synchronized PEP 440 versioning across project metadata using dynamic imports.

### Changed
- Refactored `src/osef/__init__.py` and CLI to dynamically resolve the package version from `importlib.metadata`.

---
## [0.1.0-alpha] - 2026-06-26

### Added
- **Initial Public Foundation Release.**
- **Architecture Complete:** Published Engineering Ontology Specification (EOS), Knowledge Kernel (EKK), Runtime, and Plugin architectures.
- **Developer Experience (DX):** Published 100+ mapped User Stories and 10 Playbooks.
- **Governance:** Established the OSEF Constitution, Change Control Policy, and RFC Gatekeeping processes.
- **Implementation Planning:** Published Sprint Plans, Backlogs, Coding Standards, and Dependency constraints.
- **Infrastructure:** Scaffolded standard GitHub community templates and licenses.

### Changed
- N/A (Initial Release)

### Removed
- N/A (Initial Release)

### Fixed
- N/A (Initial Release)

### Note
- **No production implementation yet.** This release signals the formal freeze of the Architecture Phase and the authorization to begin Sprint 1 implementation.

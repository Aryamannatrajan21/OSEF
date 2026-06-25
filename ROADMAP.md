# OSEF Public Roadmap

This roadmap outlines the strategic milestones leading up to the `v1.0.0` Stable release. 
*Note: For granular task-level planning, see the [Sprint Plan](implementation/SPRINT_PLAN.md).*

---

### v0.1.0-alpha: Foundation Release (Current)
- **Status:** ✅ Complete
- **Success:** Architecture, Governance, and DX specifications are publicly published. Repository is ready for contributors.

### v0.2.x: The Core Runtime
- **Status:** 🟡 In Progress
- **Success:** The Dependency Injection container and asynchronous Event Bus are operational. Internal services can communicate via events.

### v0.3.x: The Knowledge Kernel
- **Status:** ⚪ Planned
- **Success:** OSEF can parse Markdown-based EKK rules from disk into strictly typed Python domain models.

### v0.4.x: Plugin Runtime
- **Status:** ⚪ Planned
- **Success:** The architecture can dynamically discover and load third-party Python plugins via entry points, successfully hooking them into the Event Bus.

### v0.5.x: SDK & CLI Alpha
- **Status:** ⚪ Planned
- **Success:** The `osef` command-line tool is functional. Users can run `osef init` to scaffold basic configuration files.

### v0.6.x: Repository Analysis
- **Status:** ⚪ Planned
- **Success:** The Transformation Engine (OSTE) can successfully parse a target repository's ASTs and directory structure into a standard representation.

### v0.7.x: Documentation Engine
- **Status:** ⚪ Planned
- **Success:** OSEF can generate interactive, Jinja2-templated governance files (e.g., `CONTRIBUTING.md`, ADRs) based on user prompts.

### v0.8.x: OSTE MVP (Beta Release)
- **Status:** ⚪ Planned
- **Success:** The analyzer connects to the Knowledge Kernel. `osef analyze` correctly warns users about missing architectural constraints.

### v0.9.x: Release Candidate
- **Status:** ⚪ Planned
- **Success:** Certification scoring algorithms are finalized. Headless GitHub Actions execution is verified. Zero critical bugs remain.

### v1.0.0: Stable Release
- **Status:** ⚪ Planned
- **Success:** PyPI publishing. API strictly governed by Semantic Versioning. Production ready.

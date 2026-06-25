# OSEF Risk Register

This document tracks identified architectural and implementation risks, their impact, and how we mitigate them.

## 1. Architecture Drift
- **Likelihood:** Medium
- **Impact:** High
- **Description:** Developers ignore the Reference Architecture during implementation for the sake of speed.
- **Mitigation:** Strict `DEFINITION_OF_DONE.md` enforcement. Architecture Conformance tests running in CI to catch forbidden imports.

## 2. Dependency Growth
- **Likelihood:** High
- **Impact:** Medium
- **Description:** Third-party libraries are added to the core over time, slowing down startup and increasing security footprint.
- **Mitigation:** The `PYTHON_PACKAGING_DIRECTIVE.md` restricts Core to standard lib, `typer`, `pydantic`, `jinja2`. Any new dependency requires a Major RFC.

## 3. Poor Plugin Compatibility
- **Likelihood:** Medium
- **Impact:** High
- **Description:** Changes to the Core runtime frequently break third-party plugins.
- **Mitigation:** Strict `API_STABILITY_POLICY.md`. Use of generic `typing.Protocol` interfaces instead of concrete classes for plugin interaction.

## 4. Performance Regression (Parsing)
- **Likelihood:** High
- **Impact:** Medium
- **Description:** The OSTE static analyzer becomes too slow on massive monorepos.
- **Mitigation:** Enforce streaming limits in the Storage Provider. `aiofiles` for non-blocking IO. Never load full ASTs into memory for files over a certain threshold.

## 5. Documentation / EKK Drift
- **Likelihood:** Medium
- **Impact:** High
- **Description:** The Python implementation drifts from the rules declared in the Markdown EKK.
- **Mitigation:** The Python code must never hardcode business logic. It must fetch constraints dynamically from the EKK.

## 6. AI Agent Hallucination (DX Integration)
- **Likelihood:** High
- **Impact:** Medium
- **Description:** AI IDEs (Cursor/Copilot) hallucinate incorrect OSEF commands or rules despite context injection.
- **Mitigation:** Ensure the generated `.cursorrules` uses highly explicit, few-shot prompting constraints rather than vague descriptions.

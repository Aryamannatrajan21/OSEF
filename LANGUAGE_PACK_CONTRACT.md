# OSEF Language Pack Contract

To ensure that OSEF provides a consistent, universally capable engineering operating model across all tech stacks, every official **Language Pack** MUST satisfy the following certification checklist before being promoted to Tier 1 (Official) status.

## Certification Checklist

- [ ] **Parser Capability**
  - Accurately parses source code into the unified intermediate representation.
  - Gracefully handles syntax errors and partial code states.

- [ ] **Graph Generation**
  - Emits nodes and edges that fully comply with Graph Schema v5.0.
  - Properly extracts classes, functions, interfaces, variables, and dependencies.

- [ ] **Provenance Support**
  - Every generated node must accurately map back to `file`, `start_line`, `end_line`, and `column` for precision IDE and AI tooling.

- [ ] **Policy Compatibility**
  - Generates graph structures that work with the canonical cross-language Engineering Policy Engine rules.

- [ ] **Correlation Compatibility**
  - Subsystems (e.g., security findings, runtime traces) can accurately correlate against the emitted structural nodes.

- [ ] **Validation Compatibility**
  - Passes the canonical Platform Validation Engine benchmarks for its respective target repository.

- [ ] **Profile Compatibility**
  - Accurately integrates with relevant `EngineeringProfiles` (e.g., `backend`, `frontend`).

- [ ] **Certification Status**
  - Populates its `PluginCertification` object correctly, claiming compatibility with SDK v1.x and Schema v5.0.

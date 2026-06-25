# OSEF Configuration Experience Specification

## Overview
Configuration should be minimal, explicit, and versioned. Developers should not need to configure OSEF to get value from it. When configuration is required, it follows a strict, predictable hierarchy.

## 1. Minimal Defaults
OSEF ships with "Excellent Defaults." If a developer runs `osef analyze` in an empty directory, OSEF does not crash; it uses default EKK rules for a generic open-source project.

## 2. Layered Precedence
When resolving a configuration value (e.g., `audit_strictness`), OSEF checks the following layers, ordered from highest to lowest precedence:

1. **CLI Flags:** `osef analyze --strict` (Overrides everything for a single run)
2. **Environment Variables:** `OSEF_AUDIT_STRICTNESS=True` (Useful for CI/CD)
3. **Project Configuration:** `pyproject.toml` `[tool.osef]` section (Version-controlled project standards)
4. **Local Project Configuration:** `.osef/config.yaml` (Project-specific overrides, often gitignored)
5. **Global User Configuration:** `~/.osef/osef.yaml` (Developer's personal preferences)
6. **Core Defaults:** The EKK baseline.

## 3. Explicit Tracing
If a user wonders why a specific rule fired, they can run:
```bash
osef config show audit_strictness
```
The CLI must print not just the value, but *where* it was resolved from:
`audit_strictness: True (Resolved from pyproject.toml line 42)`

## 4. `pyproject.toml` First
For Python projects, OSEF prefers integrating into `pyproject.toml` rather than creating a new `osef.yaml` file, minimizing repository clutter.
```toml
[tool.osef]
profile = "library"
strictness = "high"
```

## 5. Portable Configuration
Configurations can be exported and shared. A senior engineer can run:
```bash
osef config export --target team.yaml
```
And commit this file, allowing other developers to run `osef init --from team.yaml`.

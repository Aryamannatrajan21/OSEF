# OSEF API Stability Policy

## Overview
OSEF is a platform. Breaking the Public API breaks the Plugin ecosystem, which violates our core principles.

## 1. Public API Surface
The following modules are strictly governed by Semantic Versioning (SemVer):
- `osef.contracts.*`
- `osef.interfaces.*`
- `osef.exceptions.*`
- `osef.core.context.*`
- Output formatting of `osef analyze --json`

## 2. Semantic Versioning Rules
- **MAJOR (x.0.0):** 
  - Removing a method from a `Protocol`.
  - Renaming an Event type.
  - Adding a required parameter to an interface without a default value.
- **MINOR (0.x.0):** 
  - Adding a new Event type.
  - Adding an optional parameter to the SDK.
  - New Core plugins.
- **PATCH (0.0.x):** 
  - Bug fixes in `services/` or `adapters/`.
  - CLI color tweaks.

## 3. Internal API Volatility
Modules in `osef.services.*`, `osef.adapters.*`, and `osef.cli.*` are **Internal APIs**.
- Plugins must not import from these.
- Maintainers may refactor these heavily in MINOR or PATCH releases without warning.

## 4. Deprecation Policy
Before a Public API can be removed in a MAJOR release:
1. It must be marked with the `@typing.deprecated` decorator (Python 3.13) in a MINOR release.
2. It must emit a `DeprecationWarning` at runtime.
3. A migration guide must be published.
4. It must survive for at least one full MINOR lifecycle (e.g., deprecated in `v1.2`, removed in `v2.0`).

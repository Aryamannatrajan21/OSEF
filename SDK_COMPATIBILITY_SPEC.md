# OSEF SDK Compatibility Specification

This document defines the formal compatibility guarantees, public APIs, and versioning rules for the OSEF SDK. This specification acts as the contract for all third-party developers building plugins, language packs, or intelligence agents on top of OSEF.

## 1. Public APIs

The following modules represent the **Public API** surface of OSEF v1.x. Changes to these modules are strictly governed by Semantic Versioning (SemVer) rules.

- `osef.sdk.plugin.*` (Plugin Manifests, Interfaces)
- `osef.sdk.profiles.*` (Engineering Profiles, Resolution Engine)
- `osef.sdk.registry.*` (Ecosystem Registry, Compatibility Engine)
- `osef.sdk.validation.*` (Platform Validation Engine, Reports)
- `osef.contracts.*` (Core Exceptions, Interfaces)
- `osef.intelligence.models.*` (Engineering Assessment, Findings)

## 2. Compatibility Guarantees

- **Forward Compatibility:** A plugin built for OSEF `v1.0.0` is guaranteed to function without modification in any `v1.x.x` release.
- **Graph Schema:** The Graph Schema (`v5.0`) is structurally frozen. Additions of new node/edge types are non-breaking. Changes to existing required properties are breaking changes and require a major version bump.
- **Configuration:** Profiles are declarative. Unrecognized plugins specified in a profile will be ignored or warned against, but will not crash the resolution engine.

## 3. Semantic Versioning Rules

OSEF adheres strictly to [Semantic Versioning 2.0.0](https://semver.org/).
- `MAJOR` version increments when incompatible API changes are made to the Public APIs or Graph Schema.
- `MINOR` version increments when functionality is added in a backwards-compatible manner (e.g., a new Knowledge Domain).
- `PATCH` version increments for backwards-compatible bug fixes.

## 4. Plugin Compatibility Policy

Plugins must declare their `sdk_version` and `graph_schema` compatibility bounds in their `PluginManifest`.
The `CompatibilityEngine` enforces these bounds during initialization.
If a plugin claims compatibility with `v1.0.0`, it is assumed compatible with `v1.x.x` unless specifically restricted.

## 5. Deprecation Policy

When a Public API or behavior is deprecated:
1. It will be marked with a `@deprecated` decorator and emit a runtime warning.
2. It will be documented in the SDK Release Notes.
3. It will remain fully functional for the entire lifecycle of the current major version (e.g., `v1.x`).
4. It will only be removed in the next major version release (e.g., `v2.0.0`).

# OSEF RFC Gatekeeping Policy

## Overview
Not all changes are created equal. The RFC (Request for Comments) process ensures that architectural shifts are peer-reviewed before code is written, while low-risk changes proceed without bureaucracy.

## 1. No RFC Required
*Changes that can be merged via standard PR review.*
- Bug fixes.
- Refactoring `services/` or `adapters/` that do not alter the Public API.
- Updating documentation or Playbooks.
- Adding a new isolated Plugin to the ecosystem.
- Minor performance optimizations.

## 2. Minor RFC Required
*Changes that require a brief Markdown proposal reviewed by Core Maintainers.*
- Adding a new CLI command to the Core.
- Extending an existing `typing.Protocol` with backward-compatible defaults.
- Adding new configuration keys to `pyproject.toml`.

## 3. Major RFC Required
*Changes that require community feedback and extensive architectural review.*
- Modifying the Core Initialization / Dependency Injection lifecycle.
- Changing the Ontology (`EOS.md`) or EKK schema.
- Breaking backwards compatibility in the Public API (requires MAJOR version bump).
- Changing the primary default Storage provider (e.g., from `sqlite` to `postgres`).
- Altering the scoring algorithms of the Certification Engine.

## 4. Submitting an RFC
RFCs are submitted as Pull Requests adding a document to `docs/architecture/rfc/`. 
They must include:
1. Abstract
2. Motivation
3. Proposed Architecture
4. Drawbacks
5. Alternatives
6. Unresolved Questions

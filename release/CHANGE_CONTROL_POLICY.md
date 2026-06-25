# OSEF Change Control Policy

## Overview
This policy defines the approval requirements for different classes of codebase changes during implementation and post-release.

## 1. Bug Fix
- **Definition:** Corrects behavior to match the existing specification.
- **Approval Required:** 1 Code Review from a Core Maintainer.
- **RFC Required:** No.
- **Documentation Impact:** Add to `CHANGELOG.md`.

## 2. Documentation Update
- **Definition:** Typos, Playbook updates, docstring improvements.
- **Approval Required:** 1 Code Review.
- **RFC Required:** No.

## 3. Feature Addition
- **Definition:** A new CLI flag, new output formatter, or a non-breaking SDK addition.
- **Approval Required:** 1 Code Review.
- **RFC Required:** No (unless it significantly expands scope).
- **Documentation Impact:** Must update `CLI_UX.md` or `SDK_UX.md`.

## 4. Architectural Enhancement
- **Definition:** Modifying the initialization sequence, adding new `typing.Protocol` bases.
- **Approval Required:** 2 Code Reviews from Core Maintainers.
- **RFC Required:** **Minor RFC**.
- **Documentation Impact:** Must update `ARCHITECTURE.md` and/or System Design.

## 5. Breaking Change
- **Definition:** Renaming an Event, removing a public SDK method, altering EKK schema.
- **Approval Required:** Unanimous Core Maintainer consent.
- **RFC Required:** **Major RFC**.
- **Documentation Impact:** Requires an ADR, updated documentation, and a Migration Guide. Must wait for a MAJOR version bump.

## 6. Ontology Change
- **Definition:** Modifying the root definitions of the Engineering Operating System (EOS).
- **Approval Required:** Project Founder approval.
- **RFC Required:** **Major RFC**.

# OSEF Reference Architecture

## Overview
The **OSEF Reference Architecture** is the canonical technical specification for the platform. It compiles and indexes all Phase 0 architectural, domain, and subsystem specifications into a single source of truth.

> **Constraint:** If an implementation (Python code) conflicts with the Reference Architecture, the implementation is incorrect.

---

## 1. Product & Subsystem Requirements
These documents define the "What" and "Why" of the OSEF platform.

| Document | Purpose |
|----------|---------|
| [Product Requirements (PRD)](../docs/PRD.md) | The vision, target audience, and high-level product goals. |
| [Software Requirements (SRS)](../docs/SRS.md) | The functional and performance constraints of the MVP. |
| [OSTE Specification](OSTE_SPECIFICATION.md) | Defines the Open Source Transformation Engine, scoring, and certification. |
| [EKK Architecture](EKK_ARCHITECTURE.md) | Defines the Engineering Knowledge Kernel capabilities and schemas. |

---

## 2. Core Platform Design
These documents define the "How" at a high level.

| Document | Purpose |
|----------|---------|
| [System Design](SYSTEM_DESIGN.md) | High-level topology mapping the CLI, OSTE, EKK, Event Bus, and Plugins. |
| [System Interaction Models](SYSTEM_INTERACTION_MODELS.md) | Mermaid.js diagrams of critical sequence and event flows. |
| [Event Architecture](EVENT_ARCHITECTURE.md) | The payload structure and routing logic of the Event Bus. |
| [Repository Lifecycle](REPOSITORY_LIFECYCLE.md) | How OSEF discovers, analyzes, and mutates target repositories safely. |
| [Runtime Architecture](RUNTIME_ARCHITECTURE.md) | The bootstrapper lifecycle and DI initialization. |
| [Failure Recovery Model](FAILURE_RECOVERY_MODEL.md) | Exception hierarchies and graceful degradation policies. |

---

## 3. Interfaces & Dependency Management
These documents define the API surfaces and internal code boundaries.

| Document | Purpose |
|----------|---------|
| [Service Contracts](SERVICE_CONTRACTS.md) | Abstract `typing.Protocol` contracts defining core capabilities. |
| [Domain Models](DOMAIN_MODELS.md) | The immutable dataclasses representing the state of the system. |
| [Public API Specification](PUBLIC_API_SPECIFICATION.md) | The stable interfaces for external plugins and the Python SDK. |
| [Internal API Specification](INTERNAL_API_SPECIFICATION.md) | The internal routing boundaries for Services and Adapters. |
| [Dependency Graph](DEPENDENCY_GRAPH.md) | Allowed import boundaries to prevent circular dependencies. |
| [Package Architecture](PACKAGE_ARCHITECTURE.md) | The physical layout of `src/osef/`. |

---

## 4. Build, Release, & Packaging
These documents define the ecosystem footprint.

| Document | Purpose |
|----------|---------|
| [Build & Release Architecture](BUILD_AND_RELEASE_ARCHITECTURE.md) | CI/CD, linting, semantic versioning, and publishing to PyPI. |
| [Python Packaging Spec](PYTHON_PACKAGING_SPECIFICATION.md) | Mandates `uv`, `hatchling`, and strict Core dependency minimalism. |

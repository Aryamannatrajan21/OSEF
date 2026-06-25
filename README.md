# Open Source Engineering Framework (OSEF)

> **The Architecture is Complete. Engineering Begins.**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Status: Sprint 1 Released](https://img.shields.io/badge/Status-v0.2.0--alpha-orange.svg)](PROJECT_STATUS.md)

OSEF is an AI-native engineering platform designed to transform software repositories into sustainable, production-quality open-source projects. 

It is not a documentation generator or a simple repository template. It is an **Engineering Operating System** that enforces architectural rigor, governance, and developer experience through static analysis and interactive workflows.

---

## ⚠️ Current Project Status: Engineering Foundation Complete

OSEF is in active development. We have released **v0.2.0-alpha (Sprint 1: Core Runtime Implementation)**.

**What this means:**
1. The **Architecture is 100% complete and frozen**. The vision, data models, event buses, and plugin systems are fully specified.
2. The **Developer Experience is fully designed**. Over 100 user stories and 10 playbooks have been mapped.
3. The **Engineering Foundation** (CLI, EKG Models, Dependency Injection, Event Bus, Plugin SDK) is built and released with 100% test coverage.

We value engineering quality over implementation speed. We have spent extensive time designing this system to ensure it is robust, extensible, and mathematically sound before writing production code.

See [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md) for live progress on Sprint 2.

---

## 🌟 Why OSEF Exists

Most developers know *how to code*, but struggle with *how to open source*. They reinvent licensing, contributing guides, CI/CD pipelines, architecture documentation, and release management for every new project.

OSEF fixes this by acting as the **standardization layer for open source**. It analyzes your codebase, identifies architectural and governance gaps, and interactively repairs them based on the **Engineering Knowledge Kernel (EKK)**.

---

## 🏗 Architecture Overview

OSEF is built on a strict, interface-first architecture:
- **Core Runtime:** A strictly typed Dependency Injection container and asynchronous Event Bus.
- **Engineering Knowledge Kernel (EKK):** A markdown-backed database of engineering rules and heuristics.
- **Transformation Engine (OSTE):** Parses Python ASTs to map your code against the EKK.
- **Plugin Runtime:** A highly extensible hook system allowing the community to define new rules and languages.

Read the full [Reference Architecture](architectures/REFERENCE_ARCHITECTURE.md) to understand the system.

---

## 📂 Repository Structure

OSEF is a massive engineering effort. The repository is heavily structured to separate concerns:

- `architectures/`: The core system designs and Event models.
- `knowledge/`: The Engineering Knowledge Kernel (EKK) markdown database.
- `governance/`: The Constitution and master directives.
- `dx/`: Developer Experience principles, UI/UX specs, and 100+ User Stories.
- `playbooks/`: End-to-end guides on using OSEF.
- `implementation/`: Sprint plans, backlogs, and coding standards.
- `release/`: Change control, versioning, and MVP boundaries.
- `src/osef/`: The Python production codebase.

> [!WARNING]
> **Python 3.12+ Required**
> OSEF strictly requires Python 3.12 or higher for installation and development. Attempting to install via `pip` on older environments will fail.

---

## 🛣 Development Roadmap

- **v0.1.0-alpha:** Foundation Release (Architecture Complete).
- **v0.2.0-alpha (Current):** Core Runtime & Event Bus implementation.
- **v0.5.x:** SDK & CLI Alpha.
- **v0.8.x:** Transformation Engine (OSTE) MVP.
- **v1.0.0:** Stable Release.

See the full [Public Roadmap](ROADMAP.md).

---

## 🤝 Contributing

We are actively seeking contributors! Because the architecture is completely mapped out, there is zero ambiguity about what needs to be built. 

If you love strict typing, Dependency Injection, and building developer tools, this is the project for you.

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) to understand our workflow.
2. Review the [Implementation Backlog](implementation/ENGINEERING_BACKLOG.md) to see what tasks are active in the current sprint.
3. Join the discussion in [GitHub Discussions](COMMUNITY.md).

---

## ⚖️ License & Governance

OSEF is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE).

For details on how architectural decisions are made, please refer to the [RFC Gatekeeping Policy](implementation/RFC_GATEKEEPING.md) and the [Change Control Policy](release/CHANGE_CONTROL_POLICY.md).

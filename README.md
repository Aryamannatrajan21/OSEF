# Open Source Engineering Framework (OSEF)

OSEF is the foundational ecosystem for AI-assisted software engineering. It is not just a static analysis tool—it is a comprehensive **Engineering Platform SDK** designed to parse, enrich, and analyze complex codebases while providing a fully extensible plugin architecture.

## Project Vision
Our mission is to establish the definitive **Engineering Operating System**. OSEF extracts architectural truths into an immutable graph, executes deterministic engineering policies, and provides a strict contract for the open-source community to build integrations, rules, and AI agents on top of our abstractions.

*Architecture is permanent. Features are replaceable. Contracts are forever.*

---

## Architecture Overview
The OSEF pipeline operates as a one-way transformation engine ending in the Extension Host:

1. **Repository Scanner**: Discovers the project root and metadata.
2. **Parser**: Translates source code into the canonical Symbol Table (Intermediate Representation).
3. **Semantic Enrichment Layer**: Applies heuristics to classify symbols (e.g., Services, DTOs).
4. **Engineering Knowledge Graph (EKG)**: The immutable, queryable source of truth.
5. **Engineering Policy Engine (EPE)**: Resolves rule dependencies via DAG and executes deterministic engineering policies.
6. **Engineering Assessments**: Structures EPE Findings into domain-specific facts.
7. **Extension Host & EPSDK**: The runtime that loads plugins, sandboxes execution, and exposes the SDK.

---

## Extension System (EPSDK)
OSEF Core is deliberately small. All language support, complex rules, and reporting formats are designed as **Plugins**.

External developers use the **Engineering Platform SDK (EPSDK)** to build extensions. Plugins interface securely with the platform via the `ExtensionContext`, utilizing the Event Bus and the Graph Query API without ever touching internal implementations. 

For plugin development, see our [Extension Developer Guide](docs/architecture/EXTENSION_DEVELOPER_GUIDE.md).

---

## Quick Start (CLI Overview)
*(Note: OSEF currently supports Python via the standard library `ast`).*

```bash
# Analyze the current repository
osef analyze .

# Plugins can inject custom commands:
osef security audit
osef architecture analyze
```

---

## Documentation Hierarchy
OSEF's documentation is treated as a first-class product feature:
- [Specifications Index](SPECIFICATIONS.md)
- [Architecture Index](ARCHITECTURE_INDEX.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

---

## Platform Philosophy
- **Core owns abstractions. Plugins own functionality.**
- **Never expose internal implementation details.**
- **Every public interface must be versioned.**
- **Prefer explicit contracts over conventions.**

---

## Governance & Community
- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [License](LICENSE)

*Join us in building the open standard for engineering intelligence.*

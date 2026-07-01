# OSEF Roadmap

This roadmap tracks the strategic progression of the Open Source Engineering Framework (OSEF) from foundation to the future marketplace ecosystem.

## Completed Milestones

### Phase I: Platform Engineering
- **Foundation**: Core repository initialization and language-agnostic Symbol Table (IR).
- **Repository Intelligence**: Initial discovery and extraction mechanisms.
- **Engineering Knowledge Graph (EKG)**: Immutable data structure modeling the codebase.
- **Engineering Policy Engine (EPE)**: Declarative, DAG-based rule engine.
- **Engineering Platform SDK (EPSDK)**: The `ExtensionHost` and decoupled execution context.
- **Capability-Driven Runtime**: Shift from inheritance-based providers to composable capabilities.
- **Platform Validation**: Freezing the core architecture.

### Phase II: Ecosystem Engineering (Completed)
- **Sprint 7.5 & 7.6 — Engineering Intelligence Foundation**: Finalized the Engineering Ontology. Introduced `GraphQuery` and `EngineeringReasoner` into OSEF core (`src/osef/core`).
- **Track F — Enterprise Platform**: Plugin Registry, Marketplace Protocol, Cryptographic Plugin Signing (ed25519), and CLI integration.
- **Track C — Language Packs**: Delivered reference parsers for Python, TypeScript, and Java.
- **Track A — Knowledge Domains**: Delivered reference capabilities for Software (including frameworks like FastAPI), Documentation, Infrastructure, Security, Architecture, Runtime, and Enterprise domains via the Plugin Marketplace.
- **Track B — Capability Platform Expansion**: Delivered `visualization` (including CLI tools) and `graph` plugins.
- **Track D — Cross-Domain Intelligence**: Delivered `cross-domain-intelligence` plugin for reusable correlation.

---

## Upcoming Milestones

### Phase II: Ecosystem Engineering (In Progress)
- **Track E — Engineering Intelligence**: Architecture Drift, Technical Debt, Repository Health, Dependency Risk.
- **Track G — AI Engineering Intelligence**: Repository Q&A, Architecture Assistant, Agent Collaboration (initiated via the experimental `future` plugin).

---

## Future Vision

- **Engineering Memory**: Persisting the EKG across builds to track architectural drift over time.
- **Enterprise Platform**: Distributed graph querying and cross-repository policy enforcement.
- **Cloud Services**: Hosted EPE runs integrated directly into GitHub/GitLab CI pipelines.

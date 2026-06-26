# OSEF Roadmap

This roadmap tracks the strategic progression of the Open Source Engineering Framework (OSEF) from foundation to the future marketplace ecosystem.

## Completed Milestones

### Phase 1: Foundation (v0.1.0)
- Core repository initialization.
- Strict parser abstractions and language-agnostic Symbol Table (IR).
- Extensible CLI (via Typer) and basic configuration management.

### Phase 2: Repository Intelligence (v0.2.0)
- Implementation of the **Engineering Knowledge Graph (EKG)**.
- Semantic Enrichment layer heuristics.
- Foundational Analyzers producing Engineering Assessments.

### Phase 3: Engineering Policy Engine (v0.3.0)
- Extraction of imperative analyzer rules into the declarative **Engineering Policy Engine (EPE)**.
- DAG-based rule dependency resolution and highly memoized graph queries.
- Rich `Finding` domain models with Provenance, Evidence, and Recommendations.

### Phase 4: Engineering Platform SDK (v0.4.0)
- The launch of the **EPSDK**, moving all functionality out of Core and into extensions.
- Creation of the `ExtensionHost`, `ExtensionContext`, and the decoupled Event Bus.
- Formal Capability Negotiation and Plugin Sandboxing specifications.

---

## Upcoming Milestones

### Phase 5: Ecosystem & Marketplace Validation
- **Reference Plugins**: Developing official community plugins to prove the EPSDK (e.g., Markdown Report Plugin, Security Audit Rule Pack).
- **Marketplace Launch**: Implementing the Marketplace Protocol (cryptographic signatures, plugin discovery CLI commands).
- **Multi-language Support**: Expanding parser facades to natively support TypeScript and Go via plugins.

### Phase 6: Next-Gen Engineering Intelligence
- **Engineering Query Language (EQL)**: A declarative DSL specifically designed for writing rules against the EKG.
- **Transformation Engine**: Safely mutating source code using `AutoFix` capabilities derived from EPE findings.
- **AI Engineering Agents**: Providing native SDK hooks for agentic frameworks to reason over the graph and execute transformations.

---

## Future Vision

- **Engineering Memory**: Persisting the EKG across builds to track architectural drift over time.
- **Enterprise Platform**: Distributed graph querying and cross-repository policy enforcement.
- **Cloud Services**: Hosted EPE runs integrated directly into GitHub/GitLab CI pipelines.

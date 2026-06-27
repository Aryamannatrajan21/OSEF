# OSEF Engineering Ontology

This document is the master constitution of OSEF's engineering semantics. It defines the formal boundaries, vocabularies, and contracts that allow OSEF to function as a unified Engineering Intelligence Platform.

## Engineering Intelligence Stack

```text
                Engineering Applications
                       │
                       ▼
         AI • Dashboards • Reports • IDE
                       │
                       ▼
         Engineering Policy Engine (EPE)
                       │
                       ▼
            Engineering Reasoner
                       │
                       ▼
            Correlation Engine
                       │
                       ▼
                GraphQuery API
                       │
                       ▼
        Engineering Knowledge Graph (EKG)
                       │
                       ▼
      Knowledge Domains & Language Packs
                       │
                       ▼
              Pipeline Engine
                       │
                       ▼
                 Repository Input
```

## Governance: Foundation vs. Ecosystem

OSEF enforces a strict governance model to maintain architectural discipline as the platform scales.

### Foundation (Frozen)
The core architecture is now frozen. Changes to these components require a formal RFC/ADR:
- Pipeline Engine
- Engineering Knowledge Graph (EKG)
- GraphQuery API
- Correlation Engine
- Engineering Reasoner
- Engineering Policy Engine (EPE)
- Engineering Platform SDK (EPSDK)
- Domain & Capability Registries
- The Engineering Ontology

### Ecosystem (Open)
The ecosystem is open for innovation and expansion:
- Knowledge Domains (Runtime, Enterprise, etc.)
- Language Packs
- Visualization Plugins
- Dashboards and Reports
- Enterprise Packs and CLI Extensions
- AI Agents and Assistants (consuming the Reasoner's output)

## Core Specifications
- [KNOWLEDGE_MODEL_SPEC.md](./KNOWLEDGE_MODEL_SPEC.md) - The canonical index of all Knowledge Models (Software, Documentation, Infrastructure, Security, Architecture).
- [GRAPH_RELATIONSHIP_SPEC.md](./GRAPH_RELATIONSHIP_SPEC.md) - The frozen vocabulary of all permissible edge types.
- [DOMAIN_REGISTRY_SPEC.md](./DOMAIN_REGISTRY_SPEC.md) - How domains register their capabilities and schemas.
- [GRAPH_QUERY_SPEC.md](./GRAPH_QUERY_SPEC.md) - The canonical traversal API (algorithms only, no semantics).
- [CORRELATION_ENGINE_SPEC.md](./CORRELATION_ENGINE_SPEC.md) - Rules that generate cross-domain edges.
- [ENGINEERING_REASONER_SPEC.md](./ENGINEERING_REASONER_SPEC.md) - The read-only intelligence layer that answers higher-order engineering questions.
- [ENGINEERING_ONTOLOGY_VERSION.md](./ENGINEERING_ONTOLOGY_VERSION.md) - Versioning schema for the ontology.

# Domain Registry Specification

The `DomainRegistry` enforces the template and lifecycle of Knowledge Domains within OSEF.

## Responsibility
It validates and registers `KnowledgeDomainManifest` objects provided by plugins.

## The Mandatory Domain Lifecycle
Every Knowledge Domain must implement:
1. **Knowledge Model**: Define nodes and schema.
2. **Adapters**: Parse sources into the schema.
3. **GraphDelta**: Emit standard deltas.
4. **Correlation Rules**: Bridge to other domains.
5. **Policies**: EPE rule evaluations.
6. **Projections**: Read-only models.
7. **Dashboards**: Visual metrics.
8. **CLI**: Command line extensions.
9. **Certification**: Benchmark and validation.

No future domain should deviate from this without an approved RFC.

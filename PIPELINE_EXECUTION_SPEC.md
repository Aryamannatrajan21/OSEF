# Pipeline Execution Specification

**Version**: 0.4.0 (Frozen)

This specification defines the deterministic execution model of the OSEF Pipeline Engine.

## Fundamental Principles
1. **Execution is deterministic and capability-driven.**
2. **Observation is decoupled and event-driven.**
3. **Capabilities define WHAT can execute.**
4. **Extension Host decides WHO executes.**
5. **Pipeline Engine decides WHEN execution occurs.**
6. **Event Bus announces THAT execution occurred.**

## Pipeline Stages
The Pipeline Engine advances through these stages strictly in order:

1. **Scanning**: Resolves workspace files to `RepositoryManifest`.
2. **Parsing**: Capability-driven `BaseParserProvider` invoked. Yields `SymbolTable`.
3. **Semantic Enrichment**: Type & Import resolution.
4. **Graph Construction**: Generates immutable `KnowledgeGraph`.
5. **Policy Evaluation**: Capability-driven execution of rule packs.
6. **Engineering Assessment**: Combines policies and metrics.
7. **Reporting & Visualization**: Generation of final artifacts.

## Provider Constraints
- Providers must be **stateless**.
- Execution state is exclusively owned by `PipelineContext`.
- No intermediate states travel via `EventBus` payloads.

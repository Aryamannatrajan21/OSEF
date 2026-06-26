# EPE Lifecycle

The lifecycle of an analysis run using the EPE:

1. **Instantiation**: `IntelligenceLayer` requests the default `PolicyEngine`.
2. **Registry Load**: `RuleRegistry` loads all configured `RulePack`s.
3. **Graph Ingestion**: The `PolicyEngine` wraps the `KnowledgeGraph` in a `RuleContext`.
4. **DAG Resolution**: Rules are sorted topologically via `Rule.dependencies`.
5. **Execution**: Rules are evaluated iteratively. Graph queries are cached.
6. **Aggregation**: `Finding`s are gathered into a master `RuleResult`.
7. **Assessment**: Analyzers map findings into final `EngineeringAssessment` structures.

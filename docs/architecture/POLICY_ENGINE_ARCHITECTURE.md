# Engineering Policy Engine (EPE) Architecture

The Engineering Policy Engine replaces imperative analyzer logic with a purely declarative, graph-based rule evaluation system.

## 1. Motivation
Analyzers tightly coupled to rule definitions become unmaintainable as language support grows. By separating "fact extraction" (EKG) from "policy evaluation" (EPE), OSEF supports universal rules that apply across any language.

## 2. Shared Graph Query Cache
To ensure rules remain performant, the `RuleContext` provides a memoized query API. If ten different rules query `context.get_nodes_by_type("function")`, the graph traversal only occurs once.

## 3. DAG Resolution
Rules can specify dependencies via `Rule.dependencies`. The `PolicyEngine` performs a topological sort prior to execution to guarantee rules run in a valid order (e.g., executing structural rules before complexity rules).

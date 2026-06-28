# OSEF Semantic Analysis Specification

This document defines what semantic information every language pack MUST attempt to extract. While languages implement these concepts differently, the resulting `GraphDelta` must represent them uniformly.

## 1. Required Semantic Vectors

### Imports & Exports
- Module resolution tracking.
- Re-exports and aliases.
- External vs. Internal dependencies.

### Object-Oriented Semantics
- **Inheritance:** Parent classes and abstract class implementations.
- **Interfaces & Traits:** Protocol/Interface adherence.
- **Visibility:** Public, private, protected, package-private mappings.

### Type System
- **Generics:** Type parameters and bounds.
- **Type Relationships:** Union types, intersection types, aliases.

### Metaprogramming
- **Decorators / Annotations / Attributes:** Runtime metadata bound to specific nodes.

### Dependency Graphs
- Cross-file dependency linkages.
- Project-level dependency tracking (e.g., `package.json`, `pom.xml`).

### Call Graphs
- Accurate tracking of invocations (`Software.Method -[CALLS]-> Software.Function`).

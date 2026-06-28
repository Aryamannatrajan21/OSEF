# OSEF Canonical Node Mapping

This specification defines how language-specific abstractions map to the universal `Graph Schema v5.0`.

## 1. Universal Abstractions
Different languages implement grouping and scoping differently, but the graph model must remain stable.

**Hierarchy Mapping:**
`Namespace -> Package -> Module -> Type -> Member`

## 2. Software Node Mapping (Examples)
All language plugins MUST map their constructs to the following canonical `Software.*` nodes:

- `Software.Module` (Files, exports)
- `Software.Package` (npm packages, Maven artifacts)
- `Software.Namespace` (C++ namespaces, TS modules)
- `Software.Class`
- `Software.Interface`
- `Software.Enum`
- `Software.Function` (Global or static functions)
- `Software.Method` (Bound to a class/object)
- `Software.Property` (Fields, variables on an object)
- `Software.Variable` (Local or global variables)
- `Software.TypeAlias`
- `Software.GenericParameter`
- `Software.Decorator` (Annotations, Attributes, Decorators)

## 3. Edge Mapping
- `CALLS` (Method/Function invocations)
- `INHERITS` (Class extension)
- `IMPLEMENTS` (Interface compliance)
- `IMPORTS` / `DEPENDS_ON`
- `CONTAINS` (Scoping and ownership)

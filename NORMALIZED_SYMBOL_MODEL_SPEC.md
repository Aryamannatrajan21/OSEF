# OSEF Normalized Symbol Model Specification

This document defines the canonical, language-independent representation of program elements (`NormalizedSymbolModel`) and the rules governing their resolution (`ResolvedSymbolGraph`). This contract must be satisfied by every language pack before semantic resolution and engineering fact extraction can begin.

## 1. Canonical Symbol Types

Every language plugin must translate its AST into instances of the following canonical symbols. Languages that lack specific features (e.g., Go lacks Classes) simply do not emit those types.

- `NormalizedPackage`
- `NormalizedModule`
- `NormalizedNamespace`
- `NormalizedImport`
- `NormalizedExport`
- `NormalizedClass`
- `NormalizedInterface`
- `NormalizedTrait`
- `NormalizedStruct`
- `NormalizedEnum`
- `NormalizedTypeAlias`
- `NormalizedFunction`
- `NormalizedMethod`
- `NormalizedConstructor`
- `NormalizedProperty`
- `NormalizedVariable`
- `NormalizedConstant`
- `NormalizedGeneric`
- `NormalizedDecorator`
- `NormalizedAnnotation`

## 2. Required and Optional Fields

Each normalized symbol MUST define:
- **`symbol_id`**: A deterministic, stable identifier (see section 3).
- **`kind`**: The canonical symbol type from the list above.
- **`name`**: The raw string name of the symbol (or `<anonymous>` if unnamed).
- **`provenance`**: Strict forensic metadata linking back to the source (see section 4).

Optional fields (populated when applicable):
- **`modifiers`**: `public`, `private`, `static`, `abstract`, `async`, etc.
- **`type_hint`**: Raw string representation of the declared type.
- **`docstring`**: Associated comments or documentation strings.

## 3. Stable Identifier Rules

Every symbol must receive a deterministic string identifier. UUIDs are strictly forbidden. The identifier is constructed hierarchically:

```text
<language>::<filepath>::<qualified_name>::<kind>
```

**Examples:**
- `typescript::src/services/user.ts::UserService::class`
- `java::com.example.app.User::getUsername::method`
- `go::pkg/auth/token.go::ValidateToken::function`

This ensures that the `ResolvedSymbolGraph` can deterministically link nodes even across multiple parsing passes.

## 4. Provenance Requirements

Provenance is split into two forensic categories to ensure exact traceability.

### Parsing Provenance (Attached by Parser Adapter)
```yaml
language: typescript
parser: tree-sitter-typescript
parser_version: 0.23.2
source_file: src/services/user.ts
source_hash: a1b2c3d4e5f6...
ast_node_kind: class_declaration
```

### Semantic Provenance (Attached by Semantic Engine)
```yaml
semantic_stage: resolved
resolver_version: 0.1.0
plugin_version: 0.1.0
sdk_version: 1.0.0
graph_schema_version: 5.0
normalized_symbol_id: typescript::src/services/user.ts::UserService::class
```

## 5. Resolver Expectations (The ResolvedSymbolGraph)

The Resolver consumes `NormalizedSymbol` objects and produces a `ResolvedSymbolGraph` by emitting deterministic relationships. 

**The Resolver MUST NOT produce engineering knowledge (Architecture, Security). It strictly produces language semantics.**

Valid relationship types:
- `IMPORTS`
- `DECLARES`
- `IMPLEMENTS`
- `EXTENDS`
- `OVERRIDES`
- `USES`
- `CALLS`
- `RETURNS`
- `REFERENCES`

# OSEF Language Adapter Specification

This specification defines the contract between external parsing engines (e.g., Tree-sitter, compilers, LSP servers) and the OSEF abstraction.

## 1. Parser Agnosticism
Language adapters MUST NOT hardcode their logic to a single parser backend if alternatives exist. The internal AST representation must be abstracted so that the semantic layer can consume from multiple sources.

For example, a TypeScript adapter might support:
`Tree-sitter -> Normalized AST` or `SWC -> Normalized AST`

## 2. Provenance Guarantees
Every node emitted by a language adapter MUST include exhaustive provenance metadata. Without this, downstream AI tooling cannot map insights back to source code.

Required Provenance Fields:
- `language`: The canonical language name (e.g., `typescript`)
- `parser`: The backend used (e.g., `tree-sitter-typescript`)
- `version`: The parser/compiler version
- `source_file`: Absolute or relative path to the parsed file
- `source_range`: `[start_line, start_column, end_line, end_column]`
- `ast_node_kind`: The raw token or AST node type from the underlying parser

## 3. The GraphDelta Contract
Language adapters must yield a `GraphDelta` object. They MUST NOT attempt to write directly to the persistent store or execute correlations. The adapter is strictly a producer of structured knowledge.

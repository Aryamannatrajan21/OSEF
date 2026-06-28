# OSEF Language Plugin Specification

This specification defines the lifecycle and structural contract for all official language packs in the OSEF ecosystem. 

## 1. Universal Layout
All official language plugins MUST adhere to the following directory structure:
```text
reference-plugins/<language>/
├── docs/
├── benchmarks/
├── examples/
├── fixtures/
├── src/
│   ├── parser/      # AST Generation & File Discovery
│   ├── resolver/    # Symbol Extraction & Resolution
│   ├── semantics/   # Semantic Enrichment & GraphDelta creation
│   ├── projections/ # Language-specific graph projections
│   ├── policies/    # Language-specific engineering policies
│   ├── reports/     # Language-specific assessments
│   └── cli/         # CLI extensions
├── tests/
│   ├── unit/
│   ├── integration/
│   └── certification/
├── plugin.yaml
├── pyproject.toml
└── README.md
```

## 2. Parsing Lifecycle
Every language plugin MUST implement the following pipeline stages:
1. **Discovery**: Identify relevant source files within the workspace.
2. **Parsing**: Generate the Abstract Syntax Tree (AST). Must support pluggable backends (e.g., Tree-sitter, SWC).
3. **Symbol Extraction (Resolver)**: Map AST nodes to raw language symbols.
4. **Semantic Analysis**: Enrich symbols into a canonical knowledge graph (the `GraphDelta`).
5. **Correlation**: (Handled by OSEF Core)
6. **Reasoning**: (Handled by OSEF Core)

## 3. Registration
Language plugins must declare a `LanguageCapability` in their `PluginManifest`. This capability allows the `EcosystemRegistry` to query and route language-specific tasks dynamically without manual inspection.

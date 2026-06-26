# OSEF Architecture Index

Welcome to the internal blueprint of the Open Source Engineering Framework (OSEF).

OSEF relies on immutability of design. Features can be swapped in and out via plugins, but the core abstractions (the **Architecture**) are strictly governed and completely decoupled from specific implementations.

## Architectural Journey
If you want to understand how OSEF works under the hood, read the specifications in this order:

### 1. The Core Data Model
- How we parse code: [Parser Contract](docs/architecture/PARSER_CONTRACT.md)
- The universal language: [Symbol Table Specification](docs/architecture/SYMBOL_TABLE_SPEC.md)
- The ultimate truth: [Graph Schema](docs/architecture/GRAPH_SCHEMA.md)

### 2. The Logic Layer
- How we execute rules: [Policy Engine Architecture](docs/architecture/POLICY_ENGINE_ARCHITECTURE.md)
- How rules are packaged: [Rule Pack Specification](docs/architecture/RULE_PACK_SPECIFICATION.md)

### 3. The Extension Layer
- How plugins hook in: [Extension Host Specification](docs/architecture/EXTENSION_HOST_SPEC.md)
- How plugins communicate: [Event Bus Specification](docs/architecture/EVENT_BUS_SPEC.md)
- The developer contract: [Plugin SDK Specification](docs/architecture/PLUGIN_SDK_SPEC.md)

For a complete flat list of all frozen documents, see [Specifications](SPECIFICATIONS.md).

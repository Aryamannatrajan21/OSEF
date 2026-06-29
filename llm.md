# OSEF (Open Source Engineering Framework) - Canonical AI Specification

## 1. Executive Summary
OSEF is the Engineering Operating System for AI-Assisted Software Development. Modern software engineering suffers from architectural drift, hidden dependencies, and tribal knowledge. Traditional static analysis tools operate on raw syntax (ASTs), which are fragile, language-specific, and lack semantic understanding of system architecture.

OSEF solves this by transforming unstructured source code across multiple languages into an immutable **Engineering Knowledge Graph (EKG)**. By modeling engineering domains (Software, Infrastructure, Architecture) rather than syntax, OSEF allows developers and autonomous AI agents to query, audit, and reason about codebase architecture deterministically. 

OSEF is unique because it forces all language parsers to compile down to a canonical set of engineering abstractions via a strict Language SDK, ensuring language neutrality.

## 2. Engineering Philosophy
- **Engineering Intelligence**: We model engineering concepts (Services, Dependencies, Deployments) not language tokens.
- **Deterministic Analysis**: The pipeline must produce the exact same graph for the same code.
- **Architecture over Syntax**: Abstract away language-specific quirks into universal relationships.
- **Immutable Engineering Knowledge**: The resulting EKG is a read-only, point-in-time snapshot.
- **Language Neutrality**: The core platform does not know what Python, Java, or TypeScript are.
- **Plugin-first Architecture**: All language processing happens in isolated reference plugins.
- **Zero Core Modifications**: Adding a new language must never require changing OSEF core.
- **Constitutional Governance**: Strict architectural rules (the Constitution) prevent coupling and tech debt.

## 3. High-Level Architecture
The OSEF pipeline is a unidirectional, deterministic data flow:

`Workspace`
↓
`Language Plugin` (Dynamically loaded based on workspace contents)
↓
`Parser` (tree-sitter adapters)
↓
`NormalizedAST` (Universal AST wrapper)
↓
`NormalizedSymbolModel` (Language-agnostic symbols like Classes, Interfaces)
↓
`ResolvedSymbolGraph` (Symbols connected by language-level references e.g. EXTENDS)
↓
`SemanticFacts` (Heuristic assertions e.g. "Is a Controller")
↓
`GraphMapper` (Translates facts into Delta)
↓
`GraphDelta` (Diff to be applied to the EKG)
↓
`Engineering Knowledge Graph` (The canonical state graph)
↓
`Correlation Engine` (Links entities across domains)
↓
`Engineering Reasoner` (Traverses the EKG to answer queries)
↓
`Engineering Policy Engine` (Evaluates architectural rules against the EKG)
↓
`Engineering Confidence` (A deterministic 0-100 score of pipeline/graph validity)
↓
`Validation & Certification` (Ensures plugins and core meet all specifications)

Each boundary exists to strictly decouple parsing (syntax) from reasoning (semantics).

## 4. Frozen SDK Contracts (The Source of Truth)
Autonomous agents building on OSEF must perfectly implement the following Frozen SDK interfaces (`src/osef/sdk/language/*`). DO NOT modify these.

### A. Normalized Symbol Models
Extracted by the Plugin `Extractor`, representing agnostic code structures.
```python
class ParsingProvenance(BaseModel):
    language: str
    parser: str
    parser_version: str
    source_file: str
    source_hash: str
    ast_node_kind: str
    source_range: List[int]  # [start_line, start_col, end_line, end_col]

class SemanticProvenance(BaseModel):
    semantic_stage: str
    resolver_version: str
    plugin_version: str
    sdk_version: str
    graph_schema_version: str
    normalized_symbol_id: str

class NormalizedSymbol(BaseModel):
    schema_version: str = "1.0"
    symbol_id: str
    name: str
    kind: str  # e.g., 'class', 'interface', 'function', 'package', 'module'
    parsing_provenance: ParsingProvenance
    semantic_provenance: SemanticProvenance
    modifiers: List[str] = Field(default_factory=list)
    type_hint: Optional[str] = None
    docstring: Optional[str] = None
    payload: dict = Field(default_factory=dict)
```

**Supported Kinds**: `NormalizedPackage`, `NormalizedModule`, `NormalizedNamespace`, `NormalizedImport`, `NormalizedExport`, `NormalizedClass`, `NormalizedInterface`, `NormalizedTrait`, `NormalizedStruct`, `NormalizedEnum`, `NormalizedTypeAlias`, `NormalizedFunction`, `NormalizedMethod`, `NormalizedConstructor`, `NormalizedProperty`, `NormalizedVariable`, `NormalizedConstant`, `NormalizedGeneric`, `NormalizedDecorator`, `NormalizedAnnotation`.

### B. Resolved Relationships
Emitted by the Plugin `Resolver`.
```python
class ResolvedRelationship(BaseModel):
    relationship_id: str
    source_symbol_id: str
    target_symbol_id: str
    relationship_type: str # DECLARES, EXTENDS, IMPLEMENTS, IMPORTS, CALLS
```

### C. Semantic Facts
Emitted by the Plugin `SemanticEngine` to declare universal engineering truths. Kinds include:
```python
class SemanticFact(BaseModel):
    schema_version: str = "1.0"
    subject_symbol_id: str
    fact_type: str
    attributes: Dict[str, Any] = Field(default_factory=dict)

# Specific Facts (Derived from SemanticFact):
# ContainsFact, NamespaceFact, ModuleFact, InheritanceFact, ImplementationFact
# GenericConstraintFact, TypeAliasFact, TypeUsageFact, ImportFact, ExportFact
# DependencyFact, CallFact, OverrideFact, VisibilityFact, OwnershipFact
# DocumentationFact, AnnotationFact, DecoratorFact
```

### D. Graph Delta
Emitted by the Plugin `GraphMapper`, consumed by the EKG.
```python
class NodeDelta(BaseModel):
    id: str
    type: str # Graph Ontology Node Type
    properties: dict[str, Any]

class EdgeDelta(BaseModel):
    source_id: str
    target_id: str
    relationship: str # Graph Ontology Edge Type
    properties: dict[str, Any]

class GraphDelta(BaseModel):
    schema_version: str = "1.0"
    nodes: List[NodeDelta]
    edges: List[EdgeDelta]
```

## 5. Engineering Ontology
OSEF models the world via Engineering Domains, not code domains. Nodes map to engineering concepts.
- **Software**: Classes, Interfaces, Functions, Modules.
- **Architecture**: Microservices, Gateways, Data Stores, Message Brokers.
- **Infrastructure**: Containers, Pods, Deployments.
- **Runtime**: Processes, Metrics, Traces.
- **Security**: Authentication Boundaries, Secrets.
- **Enterprise**: Teams, Ownership, Bounded Contexts.
- **Documentation**: ADRs, Specs, Walkthroughs.

By modeling engineering, OSEF allows cross-domain queries (e.g. "Which Team owns the Service that deploys the Class violating this Security Policy?").

## 6. Engineering Knowledge Graph
The EKG is a Property Graph database in memory.
- **Nodes**: Universal entities (e.g. `Class`, `Service`).
- **Edges**: Directed relationships.
- **Canonical Relationships**: `CALLS`, `IMPORTS`, `DEPENDS_ON`, `IMPLEMENTS`, `INHERITS`, `OWNS`, `DEPLOYS`, `REFERENCES`.
- **GraphDelta**: Used to mutate the EKG.
- **Correlation**: The EKG merges nodes from different plugins (e.g. linking a Kubernetes Pod to a Java Spring Boot Application) via correlation keys.

## 7. Plugin Platform
Plugins extend OSEF without core modifications.
- **Plugin SDK**: Interfaces for building plugins.
- **Plugin Manifest**: `pyproject.toml` or `plugin.yaml` defining capabilities.
- **Capabilities**: Explicit declarations of what a plugin can do (e.g., `CAPABILITY_PARSE_JAVA`).
- **Profiles**: Groupings of plugins.
- **Certification**: Plugins must pass the Certification Engine to be loaded.
- **Compatibility Engine**: Ensures plugin versions align with SDK versions.

## 8. Language Plugins
Language packs (Reference Plugins) are implementations of the Language SDK.
- **Current Support**: TypeScript, Java, Python.
- **In Progress**: Go, Rust, Kotlin, C#.
Every language MUST map into the same `NormalizedSymbol` and `SemanticFact` abstractions. An interface in Java and an interface in TypeScript are both represented identically in the EKG.
**Cross-Language Equivalence**: The Certification Engine tests that a Microservice written in Java produces the exact same topological EKG structure as the identical Microservice written in TypeScript.

## 9. Engineering Reasoning
The `EngineeringReasoner` queries the EKG.
- **Impact Analysis & Blast Radius**: Traverse inbound `DEPENDS_ON` edges to see what breaks if a node changes.
- **Dependency Chains**: Transitive closure of `CALLS` or `IMPORTS`.
- **Ownership Chains**: Mapping code to Enterprise Team nodes.
- **Language Independent**: The Reasoner uses standard EKG queries; it does not know if it is analyzing Java or Python.

## 10. Policy Engine
The **Engineering Policy Engine (EPE)** enforces architectural rules via EKG queries.
- **Policies**: Written in Python or YAML, executed as graph traversals.
- **Use Cases**: Security policies (e.g., "Controllers cannot directly access Repositories"), Dependency validation, Governance.
- **Findings**: Violations are attached to EKG nodes and lower the global Engineering Confidence score.

## 11. Validation Platform
OSEF includes a robust Validation & Certification platform.
- **Certification Engine**: Validates the entire stack against canonical engineering fixtures.
- **Platform Validation**: Ensures core components are functioning.
- **Language Validation**: Tests individual reference plugins.
- **Determinism Check**: Guarantees repeated runs yield the exact same EKG hashes.

## 12. Benchmark Platform
The Benchmark Corpus tests OSEF against real-world repositories across 4 complexity tiers.
- **Tier 1 (Small)**: FastAPI, Flask, Express, Koa, Gin, Picocli.
- **Tier 2 (Medium)**: NestJS, React, Spring PetClinic, Next.js.
- **Tier 3 (Large)**: Kubernetes, Kafka, Prometheus.
- **Tier 4 (Massive)**: Linux Kernel, Chromium, VSCode.
The Benchmark Runner evaluates Graph Nodes, Edges, Runtime, Memory, and computes the **Engineering Confidence Score** (0-100%).

## 13. Public CLI
- `osef init`: Initialize OSEF in a repository.
- `osef analyze`: Scan the repository, run plugins, and build the EKG.
- `osef report`: Output EPE findings in Markdown/JSON.
- `osef certify`: Run the Certification Engine against local plugins.
- `osef benchmark`: Execute the Benchmark Corpus.
- `osef doctor`: Validate environment and active plugins.
- `osef graph`: Export the EKG for visualization.

## 14. Constitutional Rules
**IMMUTABLE LAWS OF OSEF**:
1. **Zero Core Modifications**: Core must never be changed to support a specific language.
2. **Language Neutrality**: Core must remain entirely agnostic to underlying programming languages.
3. **SDK Stability**: The `osef.sdk` package is frozen. Breaking changes require major version bumps.
4. **Plugin Isolation**: Plugins cannot directly modify the EKG; they must emit `GraphDelta`.
5. **Object Immutability**: Normalized models and facts are read-only after creation.
6. **Pipeline Purity**: Graph generation must be deterministic and side-effect free.
7. **Stable IDs**: Every node must have a deterministic, reproducible ID based on its lineage.

## 15. AI Agent Instructions
When writing code for OSEF, autonomous agents MUST obey:
- **Never bypass the Language SDK.** Do not write custom parsers that inject straight into the EKG.
- **Never modify frozen contracts.** (`src/osef/sdk/*`)
- **Never create parser-specific engineering objects.** (e.g., no `JavaClassNode`).
- **Never create language-specific SemanticFacts.**
- **Never modify the Engineering Ontology.**
- **Never introduce Graph Schema changes without constitutional approval.**

**IF A FROZEN ARCHITECTURE MUST CHANGE**:
STOP.
Generate an `ArchitectureReviewProposal.md`.
Do not continue implementation until user approval.

## 16. Repository Layout
- `docs/`: Frozen architectural contracts, specifications, and ADRs.
- `src/osef/core/`: The central EKG, Pipeline Orchestrator, and Reasoner.
- `src/osef/sdk/`: The frozen boundaries, models, and Plugin SDK.
- `src/osef/cli/`: Typer-based command-line interface.
- `src/osef/epe/`: Engineering Policy Engine.
- `reference-plugins/`: Official language implementations (`java`, `typescript`, `python`).
- `tests/`: End-to-end certification and unit tests.
- `benchmarks/`: The performance and scaling validation corpus.

## 17. Release Information
- **Project**: OSEF
- **Version**: 1.0.0
- **Release**: LTS
- **SDK Version**: 1.0
- **Graph Schema Version**: 1.0
- **Ontology Version**: 1.0
- **Plugin API Version**: 1.0
- **Constitution Version**: 1.0
- **LTS Status**: Active
- **Architecture Status**: Frozen

## 18. Common Engineering Questions OSEF Can Answer
- What depends on this microservice?
- Who owns this component in the Enterprise graph?
- What breaks if this interface signature changes (Blast Radius)?
- Which architectural rules are currently violated by this Pull Request?
- How do these two services communicate?
- Which bounded contexts have excessive coupling?

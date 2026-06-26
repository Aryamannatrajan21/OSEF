# OSEF Changelog

All notable changes to this project will be documented in this file. 
We track releases by major Architectural Milestones rather than granular commits.

## [v0.4.0] - Engineering Platform SDK (EPSDK)
The transition from an internal monolith to an extensible Plugin Ecosystem.
- **Added**: `ExtensionHost` and `ExtensionContext` as the sandbox for plugin execution.
- **Added**: SemVer-based Capability Negotiation for plugins.
- **Added**: Synchronous Event Bus (`osef.sdk.events`) for out-of-band analytics.
- **Added**: 19 frozen architectural contracts defining the EPSDK, Sandboxing, and Marketplace models.
- **Changed**: Core OSEF internals are permanently hidden; all extensions must interface via `osef.sdk.*`.

## [v0.3.0] - Engineering Policy Engine (EPE)
The extraction of hard-coded analyzer logic into a declarative rule evaluation system.
- **Added**: The Engineering Policy Engine (EPE) with DAG-based dependency resolution.
- **Added**: Shared Graph Query Cache for memoizing O(N) graph traversals across hundreds of rules.
- **Changed**: Analyzers stripped of rule logic, acting solely as mappers for EPE `Finding` objects.
- **Added**: Rich `Finding` models featuring Provenance, Evidence, Recommendations, and AutoFix flags.

## [v0.2.0] - Repository Intelligence
The establishment of the universal data structure.
- **Added**: The Engineering Knowledge Graph (EKG) as the single source of truth.
- **Added**: Semantic Enrichment Layer to classify basic AST nodes into structural concepts (Services, DTOs).
- **Added**: Preliminary Engineering Assessments for Architecture, Dependencies, and Documentation.

## [v0.1.0] - Foundation
The initial scaffolding of OSEF.
- **Added**: Language-agnostic Symbol Table (Intermediate Representation).
- **Added**: Basic Python AST parser.
- **Added**: Typer-based CLI interface.

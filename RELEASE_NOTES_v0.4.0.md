# Release Notes: v0.4.0 (The EPSDK Release)

**Release Date:** Sprint 4 Closeout
**Version:** 0.4.0

## The Extensibility Update
OSEF v0.4.0 marks the most significant architectural evolution since the creation of the Engineering Knowledge Graph. We have fundamentally restructured OSEF from an internal, tightly-coupled analysis application into the **Engineering Platform SDK (EPSDK)**.

This release officially establishes the OSEF Plugin Ecosystem. 

## Key Architectural Changes
- **The Core Boundary**: All internal implementations have been moved behind a strict access boundary (`osef.sdk.internal`). Plugin authors now interface exclusively with the versioned `osef.sdk` package.
- **Extension Host**: A hardened runtime environment that handles plugin discovery, lifecycle management, and Capability Negotiation.
- **Event Bus**: An asynchronous, decoupled publish/subscribe architecture allowing plugins to hook into lifecycle events (`BeforeParsing`, `AfterGraphGeneration`).
- **Graph Query API Promotion**: The internal graph traversal methods have been unified into a highly-memoized, publicly accessible `GraphQuery` object.

## Depreciation Notices
- The legacy `Analyzer` interfaces have been entirely stripped of rule evaluation logic. All rule logic must now be written as part of the **Engineering Policy Engine (EPE)**.
- Direct instantiation of `KnowledgeGraph` without the `ExtensionContext` is now deprecated for external extensions.

## Documentation Freeze
To support this massive structural shift, we have completely overhauled the repository documentation and frozen **19 Architectural Contracts**.

Please review the new [Specifications Index](SPECIFICATIONS.md) to understand the strict Sandboxing, Trust Models, and Capabilities required by the new Marketplace Protocol.

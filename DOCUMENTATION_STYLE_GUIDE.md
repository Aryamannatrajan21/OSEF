# OSEF Documentation Style Guide

Consistency in terminology and structure is paramount. Documentation is treated as a core product feature.

## 1. Terminology Constraints
Never mix historical terminology with current architecture. Always use the following canonical terms:
- **Engineering Knowledge Graph (EKG)** (Never: *Graph*, *Knowledge Graph*)
- **Engineering Policy Engine (EPE)** (Never: *Rule Engine*, *Policy Orchestrator*)
- **Engineering Platform SDK (EPSDK)** (Never: *OSEF SDK*, *Plugin API*)
- **Extension Host** (Never: *Plugin Manager*, *Host System*)
- **Extension Context** (Never: *Plugin Context*)
- **Plugin** or **Extension** (Interchangeable, but prefer Plugin for distribution and Extension for architecture).

## 2. Version Synchronization
Every architectural document must explicitly specify the compatible versions:
- SDK Version (e.g., `v0.4.0`)
- Graph Schema Version (e.g., `v4.0.0`)
- Policy API Version (e.g., `v2.0.0`)

## 3. Diagrams
All diagrams must be written using Mermaid.js syntax. Nodes must reflect the precise component names outlined in the Terminology Constraints.

## 4. Hierarchy
Markdown documents should reside in their designated directories:
- `/docs/architecture/`: Frozen specifications and architectural contracts.
- `/docs/getting-started/`: Guides for new users and contributors.
- `/docs/sdk/`: Reference materials for EPSDK.
- `/governance/`: RFCs, ADRs, and constitutional documents.

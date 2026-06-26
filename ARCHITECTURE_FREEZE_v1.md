# Architecture Freeze Declaration (v1.0.0-rc)

**Date**: Sprint 5B
**Subject**: Core Pipeline and SDK Execution Runtime

## Declaration of Immutability
Effective immediately, the Capability-Driven Engineering Runtime architecture is considered **FROZEN**. No further structural changes are permitted to the Core execution model without a formal Request For Comments (RFC) and Architecture Decision Record (ADR).

## Frozen Components
1. **Pipeline Engine (`src/osef/core/pipeline.py`)**
   - The sequential execution stages (Scan -> Parse -> Semantic -> Graph -> Policy) are immutable.
2. **Extension Host (`src/osef/sdk/host/`)**
   - The plugin discovery and activation lifecycle is immutable.
3. **Capability Registry (`src/osef/sdk/registry.py`)**
   - The provider resolution algorithm (Capability -> Language -> Constraint) is immutable.
4. **PipelineContext (`src/osef/sdk/pipeline.py`)**
   - The boundaries of the execution contract are immutable. (Additions are allowed; breaking changes are forbidden).
5. **Event Bus (`src/osef/sdk/events.py`)**
   - The `EventBus` is strictly restricted to passive observation. It is permanently banned from RPC and execution payload transport.

## Governance Override
Any attempt to violate these frozen constraints to patch a bug must be escalated. The SDK must be fixed, not bypassed. 

# OSEF Architecture State

## Frozen Systems (Require RFC/ADR to change)
- **Repository Scanner:** Standardized discovery.
- **Core Contracts**: `EKGBuilder` has transitioned to `PipelineEngine`. Language-specific parsing logic has been stripped from the core pipeline orchestration.
- **Extensibility Model**: OSEF is a Capability-Driven Engineering Runtime. The `ExtensionHost` with its `CapabilityRegistry` resolves stateless providers (e.g., `BaseParserProvider`) to execute via the `PipelineContext`.
- **Event Bus Role**: Reduced to pure passive observation for metrics, telemetry, and analytics.
- **Engineering Knowledge Graph (EKG):** Graph Schema `v4.0.0`.
- **Engineering Policy Engine (EPE):** Declarative rule orchestration.
- **Engineering Platform SDK (EPSDK):** `ExtensionHost`, `ExtensionContext`, Event Bus.

*Core architecture is intentionally decoupled. Extensions must implement functionality.*

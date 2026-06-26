# OSEF Architecture State

## Frozen Systems (Require RFC/ADR to change)
- **Repository Scanner:** Standardized discovery.
- **Parser Contracts:** Language-agnostic extraction.
- **Symbol Table:** Canonical Intermediate Representation (IR).
- **Engineering Knowledge Graph (EKG):** Graph Schema `v4.0.0`.
- **Engineering Policy Engine (EPE):** Declarative rule orchestration.
- **Engineering Platform SDK (EPSDK):** `ExtensionHost`, `ExtensionContext`, Event Bus.

*Core architecture is intentionally decoupled. Extensions must implement functionality.*

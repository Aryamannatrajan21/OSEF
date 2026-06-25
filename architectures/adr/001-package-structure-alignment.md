# ADR 001: Package Structure Alignment for Sprint 1

## Status
**Proposed**

## Context
The project has reached Phase 1 (Implementation), and Sprint 1 authorization has been granted. The Sprint 1 directive explicitly commands the creation of a package structure (`src/osef/`) with the following top-level modules:
- `runtime/`
- `core/`
- `events/`
- `contracts/`
- `config/`
- `logging/`
- `exceptions/`
- `bootstrap/`
- `utils/`

However, the frozen **`PACKAGE_ARCHITECTURE.md`** and **`DEPENDENCY_GRAPH.md`** dictate a strict 5-layer architecture with the following top-level modules exclusively:
- `contracts/`
- `interfaces/`
- `services/`
- `adapters/`
- `core/`
- `cli/`

The Master Execution Prompt states: *"Architecture is authoritative. Implementation must never contradict documentation. If implementation reveals architectural issues: Stop, Document the issue, Generate an ADR, Wait for approval."*

## Options Considered

### Option 1: Map Sprint 1 Components to the Frozen Architecture (Recommended)
Instead of creating flat top-level domains for `events`, `exceptions`, `logging`, etc., we map them to the existing architectural layers:
- `exceptions` → `contracts/exceptions.py` (Layer 1)
- `config` → `core/config.py` (Layer 4)
- `bootstrap` & `runtime` → `core/bootstrapper.py` and `core/container.py` (Layer 4)
- `events` → `contracts/events.py` (models) and `services/events.py` (EventBus implementation) (Layers 1 & 3)
- `logging` → `adapters/logger.py` or injected via `core/`
- `utils` → Avoided entirely (utility classes are a code smell; logic should belong to specific services).

**Pros:** Preserves the strict dependency graph. Avoids unfreezing the architecture. Maintains clear separation of concerns.
**Cons:** Requires overriding the explicit folder list provided in the Sprint 1 directive.

### Option 2: Unfreeze and Amend the Architecture
We unfreeze `PACKAGE_ARCHITECTURE.md` and `DEPENDENCY_GRAPH.md` to reflect the flat, modular structure requested in the Sprint 1 directive.

**Pros:** Directly satisfies the textual instruction of the Sprint 1 prompt.
**Cons:** Violates the "Architecture is authoritative" rule. A flat structure makes circular dependencies much harder to prevent and violates the "Minimal Core, Extensible Edge" layering strategy established in Phase 0.

## Decision
Waiting for Governance Lead approval on the proposed path. Option 1 is strongly recommended to protect architectural integrity.

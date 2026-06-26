# OSEF Known Limitations

This document tracks intentional boundaries and known limitations. It separates design constraints from actionable Technical Debt (which belongs in `TECH_DEBT.md`).

## Current Language Support
- **Python**: Fully supported via the standard library `ast`.
- **TypeScript**: Planned (Sprint 6).
- **Go**: Planned (Sprint 6).
- *Limitation*: OSEF currently cannot parse cross-language monorepos natively.

## Parser Limitations
- We use standard library `ast` for Python. This means we do not natively capture whitespace, comments (other than docstrings), or exact character offsets out-of-the-box in the IR without external tooling (like `libcst`).
- *Limitation*: OSEF cannot perform precise structural formatting/auto-fixing of syntax without third-party plugins.

## Platform Limitations
- The Engineering Policy Engine (EPE) currently runs entirely in-memory. Memory usage will scale linearly with repository size.
- *Limitation*: Repositories over 5M LoC may require breaking the graph into sub-domains.

## SDK Limitations
- The `EventBus` is strictly synchronous to guarantee deterministic execution order during policy runs.
- *Limitation*: Asynchronous plugins must manage their own event loops out-of-band and cannot block the EKG builder.

## Marketplace Status
- The Marketplace Protocol is designed but not yet implemented.
- *Limitation*: Plugins must currently be installed locally via PyPI or direct source inclusion in the `pyproject.toml`.

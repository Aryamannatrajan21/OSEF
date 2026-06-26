# Pipeline Engine Certification

**Status**: Certified
**Version**: 0.4.0
**Architectural Role**: Deterministic Orchestrator (Formerly `Pipeline Engine`)

## Validated Criteria
- `[x]` Orchestrates immutable execution stages.
- `[x]` Contains NO language-specific internal execution logic.
- `[x]` Passes `PipelineContext` cleanly to capabilities.
- `[x]` Properly invokes fallback legacy parsers gracefully if Registry misses.
- `[x]` Synchronously retrieves `SymbolTable` from providers.

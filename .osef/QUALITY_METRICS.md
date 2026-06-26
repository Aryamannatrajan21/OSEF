# OSEF Quality Metrics

Tracked metrics across releases to ensure stability and continuity.

## Current Release: v0.4.0 (EPSDK)

- **Test Coverage:** 100% (Core SDK), 95% (Parsers/EPE).
- **Typing Status:** Strict typing enforced (`mypy --strict`). 0 unresolved errors.
- **Lint Status:** Clean (`ruff check .`, `ruff format .`). 0 unresolved errors.
- **Security Status:** Passes basic dependency vulnerability scans.
- **Documentation Coverage:** 100% of Public API and Architectural Contracts are frozen in `docs/architecture/`.
- **Architecture Compliance:** EPSDK explicitly isolates Core from Extensions.
- **Public API Stability:** Unstable (Alpha phase). Stable `osef.sdk` interfaces pending `v1.0.0`.
- **Plugin Compatibility:** Enforced via SemVer Capability Negotiation (SupportsSDK `v0.4.0`).
- **Performance Benchmarks:** Target parsing speed: >10k LOC / second. (Pending formal profiling).

*Update this after every release to prevent degradation.*

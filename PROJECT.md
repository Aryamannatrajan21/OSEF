# Project: OSEF Phase III (Wave 1 & 2 Combined)

## Architecture
OSEF is a platform for codebase architecture analysis and engineering intelligence. The codebase consists of:
- **Core (src/osef/core)**: Contains the Engineering Knowledge Graph (EKG) and Engineering Reasoner.
- **EPE (src/osef/epe)**: Engineering Policy Engine evaluating rules and packs against the codebase.
- **SDK (src/osef/sdk)**: Plugin base structures and Extension Host.
- **CLI (src/osef/cli)**: Command line interface entry points built with Typer.
- **MCP Server (src/osef/mcp)**: Model Context Protocol server exposing graph queries to AI agents.
- **Studio (osef-studio)**: Next.js frontend workbench for OSEF visualizations.
- **VS Code Extension (vscode-extension)**: Client extension for OSEF tooling within VS Code.

## Code Layout
- `src/osef/cli/marketplace.py`: Marketplace CLI commands (`osef marketplace build`).
- `src/osef/cli/benchmark.py`: Benchmark CLI commands (`osef benchmark publish`).
- `src/osef/cli/policy.py`: Policy CLI commands (`osef policy check`).
- `src/osef/sdk/validation/`: Validation and certification engines.
- `src/osef/sdk/reports/`: SARIF and JUnit format exporters.
- `src/osef/mcp/`: MCP Server package (`server.py`, `context.py`).
- `vscode-extension/`: VS Code extension workspace.
- `osef-studio/`: OSEF Studio frontend React workspace.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| M1 | E2E Test Suite | Build opaque-box E2E test suite (Tiers 1-4) & publish `TEST_READY.md` | None | IN_PROGRESS (c21f5e16-d112-4701-a782-b1b1e17125aa) |
| M2 | R1: Marketplace & Leaderboard | Implement CLI generators for marketplace and benchmark publishing | None | IN_PROGRESS (96ff40c5-7e12-4fc4-ae69-60cdcdfebea3) |
| M3 | R2: CI/CD & SARIF Integration | CLI validation with `--ci`, `certify`, `policy check`, export SARIF/JUnit | None | IN_PROGRESS (96ff40c5-7e12-4fc4-ae69-60cdcdfebea3) |
| M4 | R3: MCP Server & Context | MCP Server & Context Injection layers for AI Agent integration | None | IN_PROGRESS (96ff40c5-7e12-4fc4-ae69-60cdcdfebea3) |
| M5 | R4: VS Code & Studio Workbench | VS Code extension and expand Studio workbench UI tabs/visuals | None | IN_PROGRESS (96ff40c5-7e12-4fc4-ae69-60cdcdfebea3) |
| M6 | E2E Pass & Hardening | Pass 100% of E2E test suite and run adversarial Tier 5 tests | M1, M2, M3, M4, M5 | PLANNED (96ff40c5-7e12-4fc4-ae69-60cdcdfebea3) |

## Interface Contracts
### CLI ↔ Marketplace/Benchmark Generator
- `osef marketplace build --dir <dir>`: Reads manifests, validates signature, generates static HTML/JSON site bundles.
- `osef benchmark publish --repo <repo>`: Generates a JSON leaderboard grading tech debt and architecture drift.

### EKG/Reasoner ↔ MCP Server
- MCP Tools expose `query_blast_radius(symbol: str) -> dict` and `query_dependency_path(start: str, end: str) -> list`.
- Returns semantic facts instead of raw code dumps.

### Policy Engine ↔ SARIF Report Exporter
- `PolicyEngine.evaluate()` outputs violations mapped to `SarifReport` structure conforming to SARIF 2.1.0 JSON schema.

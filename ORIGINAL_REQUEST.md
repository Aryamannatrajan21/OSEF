# Original User Request

## Initial Request — 2026-07-02T17:58:39+05:30

Implement Phase III (Wave 1 & 2 Combined) to transform OSEF into a standardized ecosystem and AI-native platform. This includes building production-level implementations across 6 major pillars: (1) Community Marketplace & Public Benchmark Leaderboard, (2) CI/CD automated validation with SARIF/GitHub Actions, (3) AI Agent Model Context Protocol (MCP) server & Context Injection, and (4) VS Code / Studio Workbench integrations.

Working directory: /Users/macair/Documents/OSEF
Integrity mode: development (Clean code integrity and best practices enforced)

## Requirements

### R1. Community Marketplace & Public Benchmark Leaderboard
Implement CLI generators (`osef marketplace build`, `osef benchmark publish`) that validate plugin packages, evaluate canonical repositories, and output static HTML/JSON site bundles suitable for GitHub Pages hosting.

### R2. CI/CD Automated Validation & SARIF Integration
Provide automated CI validation workflows and CLI commands (`osef validate --ci`, `osef certify`, `osef policy check`) that output standardized SARIF 2.1.0 and JUnit reports to detect and block architectural drift in pull requests.

### R3. AI Agent MCP Server & Context Injection
Build a Model Context Protocol (MCP) server and context injection layer enabling autonomous AI assistants (e.g., Cursor, Claude, Antigravity) to deterministically query the Engineering Knowledge Graph (EKG) and Engineering Reasoner for blast radius, dependency paths, and policy failures without parsing raw source files.

### R4. VS Code & OSEF Studio Workbench Integrations
Deliver a VS Code extension package and expand the OSEF Studio workbench UI to provide inline architectural drift reporting, instant blast radius visualization, interactive repository Q&A, and comprehensive workbench tabs (Overview, Graph, Architecture, Reasoning, Policies, Benchmarks, Plugins, Marketplace).

## Acceptance Criteria

### Marketplace & Leaderboard Verification
- [ ] Running `osef marketplace build` against a directory of valid plugin manifests successfully generates an indexed static HTML/JSON site bundle without errors.
- [ ] Running `osef benchmark publish` against test/reference repositories produces a structured leaderboard artifact grading technical debt, architecture drift, and dependency health.

### CI/CD & SARIF Verification
- [ ] Executing CLI validation commands with `--ci` or `--format sarif` produces valid SARIF 2.1.0 output that passes schema validation.
- [ ] Running validation against a repository containing an injected architectural policy violation exits with a non-zero status code and accurately identifies the violating symbols.

### AI MCP Server Verification
- [ ] The MCP server initializes cleanly and successfully returns structured JSON responses to standard tool invocations (e.g., querying blast radius or dependency paths) using test EKG fixtures.
- [ ] Context injection tools return deterministic semantic facts and reasoning outputs rather than raw code dumps.

### IDE & Studio Workbench Verification
- [ ] The VS Code extension bundle/package builds successfully and interfaces cleanly with OSEF analysis services.
- [ ] The OSEF Studio web application renders all workbench tabs and correctly visualizes graph data from local EKG snapshots.

# OSEF Repository Lifecycle

## Overview
This specification defines how OSEF interacts with a target repository. It ensures that OSEF operates predictably, respects user boundaries, and does not corrupt source code.

## 1. Lifecycle Phases

### 1. Discovery
When OSEF is invoked inside a directory, it first performs discovery:
- **Root Identification:** Looks for `.git`, `pyproject.toml`, `package.json`, or an explicit `.osef` configuration directory.
- **Context Generation:** Determines the repository profile (e.g., Python Library vs Node Web App) to select the correct Engineering Evaluation Rules from the EKK.

### 2. Static Analysis (Read-Only)
OSTE executes its analysis logic.
- **File System Parsing:** The Storage Adapter reads project structure.
- **AST/Metadata Parsing:** Language-specific plugins parse dependency files (e.g., `requirements.txt`).
- **Memory Constraint:** Large files are streamed or ignored. Entire source trees are *never* loaded fully into memory.
- **Output:** The Event Bus emits `RepositoryAnalyzed`, caching the resulting ASTs or metrics locally to prevent rescanning.

### 3. Mentorship & Prompts (Interactive)
If invoked via `osef open-source`, OSEF begins an interactive session.
- **Constraint:** Context prompts must be answered by the user before OSEF generates complex architectural decisions like Licenses or Governance models.

### 4. Mutation (Write Operations)
OSTE generates files (e.g., `ADR-0001.md`, `CODE_OF_CONDUCT.md`).
- **Safety Rule 1:** OSEF *never* overwrites an existing file without explicit user confirmation.
- **Safety Rule 2:** OSEF prefers generating files in isolated locations (e.g., `docs/architecture/adr/`) rather than mutating application source code.
- **Safety Rule 3:** OSEF emits `ProjectMutated` events so plugins can format or lint the generated output.

### 5. Finalization
The `osef` invocation ends.
- Cached metadata is persisted to `.osef/cache/` for future deterministic runs.

## 2. CI/CD Lifecycle
In CI/CD (e.g., GitHub Actions), the lifecycle is strictly limited to **Phases 1 and 2**. 
- OSEF operates in a headless, read-only mode to produce a `CertificationScore` or fail a PR based on validation rules. Mutation is disabled.

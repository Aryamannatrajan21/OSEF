# OSEF Command Design Guidelines

## Overview
Commands are the primary verbs of the OSEF ecosystem. Their design must be predictable, aligned with engineering workflows, and structured consistently.

## 1. Command Taxonomy
OSEF commands strictly follow a `verb noun` taxonomy.

- **`verb`**: The action being performed (`analyze`, `repair`, `certify`, `export`).
- **`noun`**: The target of the action (`repo`, `context`, `plugin`).

*Example:* `osef analyze repo`
For the most common workflows, the noun can be omitted if it defaults to the current context. `osef analyze` defaults to `osef analyze repo .`.

## 2. Core Verbs
The following verbs are reserved and should maintain consistent semantics across all plugins:
- **`init`**: Initialize or scaffold configuration.
- **`analyze` / `audit`**: Perform read-only static analysis.
- **`certify`**: Generate a formal evaluation or score.
- **`repair` / `fix`**: Mutate the repository to resolve issues.
- **`export`**: Output data for external tools (e.g., `.cursorrules`).
- **`search` / `query`**: Read from the EKK.

## 3. POSIX Compliance
Command line flags must adhere to standard POSIX conventions to ensure predictability for experienced terminal users.
- Use `--help` (not `-h` which could be confused with host).
- Use `--verbose` / `-v` for logging depth.
- Use `--dry-run` to simulate mutations without writing to disk.
- Use `--force` / `-f` to bypass confirmation prompts.

## 4. Addressing "What" and "Why"
Every command implementation must include a rich docstring that is parsed by `Typer` to generate the `--help` menu. It must answer:
1. **What does this do?** (Short summary)
2. **Why would I use it?** (Use case)
3. **What changed?** (Expected output or side effects)

## 5. Plugin Commands
Plugins cannot overwrite Core verbs. Plugins must register their commands under a noun group if they introduce new concepts.
*Example:* `osef security-audit` is a plugin command group.

## 6. Output Determinism
A command run twice with the same inputs on the same repository state must yield the exact same exit code and standard output. Flaky commands degrade trust.

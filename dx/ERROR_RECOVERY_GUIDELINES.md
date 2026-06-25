# OSEF Error Message & Recovery Guidelines

## Overview
Errors in OSEF are not just failure states; they are educational opportunities. Cryptic stack traces violate the Developer Experience principles. Every error message must guide the user back to a successful state.

## 1. The Tripartite Error Structure
Every error message raised to the user via the CLI must answer three questions:

### 1. What happened?
State the failure clearly in plain English. Avoid internal framework jargon.
*Bad:* `DatabaseError: Could not bind parameter.`
*Good:* `Failed to load the Engineering Knowledge Kernel.`

### 2. Why did it happen?
Provide context based on the specific variables that caused the error.
*Bad:* `File not found.`
*Good:* `The required configuration file 'pyproject.toml' could not be found in the current directory ('.').`

### 3. How to fix it?
Suggest a direct, actionable command or documentation link.
*Bad:* `Check your setup.`
*Good:* `Run 'osef init' to automatically generate a basic configuration file.`

## 2. Example: A Perfect Error Message
```text
Error: Cannot analyze project architecture.
Reason: OSEF detected a Python project, but could not find a 'requirements.txt' or 'pyproject.toml' to analyze dependencies.
Fix: 
  - If this is a Python project, run 'uv init' or 'pip freeze > requirements.txt'.
  - If OSEF misidentified the project, run 'osef analyze --profile <type>'.
```

## 3. Stack Traces
Raw Python tracebacks are frightening to users and irrelevant unless they are debugging the OSEF core itself.
- **Default:** Tracebacks are suppressed. Only the Tripartite message is shown.
- **Opt-In:** Tracebacks are printed if the user passes `--verbose` or `--debug`.

## 4. Recoverable vs Unrecoverable
- **Recoverable:** If OSEF detects a recoverable state (e.g., missing configuration), it should prompt the user to fix it interactively. "Missing .osef directory. Create one now? (Y/n)"
- **Unrecoverable:** If the user lacks filesystem permissions, fail cleanly, explain the permission issue, and exit. Do not try to forcefully mutate the system.

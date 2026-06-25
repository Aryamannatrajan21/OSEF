# OSEF CLI User Experience Specification

## Overview
The CLI is the primary interface for most developers interacting with OSEF. Its design must prioritize discoverability, speed, and approachability.

## 1. Installation
The CLI should be installable globally via `pipx` or `uv`:
```bash
uv tool install osef
```

## 2. First Command Experience
Running `osef` with no arguments should not throw an error. It should display a welcoming, cleanly formatted help menu that categorizes commands logically, not alphabetically.

```text
OSEF: The Open Source Engineering Framework

Usage: osef [OPTIONS] COMMAND [ARGS]...

Repository Workflow:
  init       Initialize OSEF in the current directory.
  analyze    Scan the repository against EKK rules.
  certify    Generate an Open Source Certification Score.
  repair     Automatically fix identified architectural issues.

Ecosystem:
  plugins    Manage OSEF plugins (install, list, remove).
  rules      Browse or query the Engineering Knowledge Kernel.

Options:
  --help     Show this message and exit.
```

## 3. Discoverability
Every command must support `--help`. The help text must include:
- A clear description of what the command does.
- At least two realistic examples.
- Available flags with their default values.

## 4. Interactive vs. Non-Interactive Modes
- **Interactive (Default):** If `osef init` detects missing configuration, it drops into a conversational prompt (using `questionary` or `Rich` prompts) to guide the user.
- **Non-Interactive (CI/CD):** If the `--ci` or `--non-interactive` flag is passed, or if OSEF detects a non-TTY environment, it falls back to defaults or fails clearly if required data is missing. It *never* hangs waiting for input in CI.

## 5. Output Formatting
- **Colors:** Use colors semantically. Red for errors, Yellow for warnings, Green for success, Blue for informational context.
- **Tables:** Use `Rich` tables for structured data (e.g., listing plugins, displaying analysis results).
- **Progress:** Use `Rich` spinners and progress bars for long-running operations (AST parsing, EKK queries).

## 6. Autocomplete
The CLI must support shell autocomplete out of the box for `bash`, `zsh`, and `fish`, generated via Typer.

## 7. Confirmation Prompts
Destructive actions (e.g., `osef repair` modifying files) must prompt for confirmation unless `--force` is provided.

```text
? OSEF is about to modify 3 files to resolve structural issues. 
Do you want to proceed? (y/N)
```

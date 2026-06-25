# OSEF Interactive Workflow Specification

## Overview
OSEF is not just a linter; it is an expert system. When faced with ambiguity, it should engage the developer in a conversational workflow rather than failing or silently making assumptions.

## 1. The Conversational Standard
Interactive prompts are built using rich terminal UI libraries (like `questionary` or `Rich`). They must support:
- Arrow-key navigation.
- Type-to-filter for long lists.
- Clear default selections.

## 2. Example Workflows

### Project Initialization (`osef init`)
Instead of demanding a complex configuration file, `osef init` asks targeted questions:
> "I see a `package.json`. Is this a frontend React app or a Node backend?"
> "Do you intend to publish this to npm, or is it private?"

### Architecture Review (`osef repair`)
When OSEF detects a missing security policy, it does not just write a generic file.
> "Your repository lacks a Security Policy (SECURITY.md)."
> "Would you like to generate one?"
> "Please enter the email address for reporting vulnerabilities: [default: security@example.com]"

### Plugin Installation
> "This repository uses the `osef-django` plugin, but it is not installed locally."
> "Would you like to install it now via `uv`? (Y/n)"

## 3. CI/CD Safety (Non-Interactive Mode)
Interactive workflows are strictly disabled in CI environments. OSEF detects CI via standard environment variables (`CI=true`, `GITHUB_ACTIONS`). 

If an interactive workflow is triggered in CI and the required flags are not present, OSEF must:
1. Log a clear error explaining *why* it cannot proceed.
2. Specify the exact CLI flags needed to bypass the prompt.
3. Exit with status code `1`.

## 4. Progressive Disclosure in Prompts
Do not overwhelm the user with 20 questions. Ask the minimum required to provide value. If advanced configuration is needed, tuck it behind a final prompt:
> "Would you like to configure advanced audit settings? (y/N)"

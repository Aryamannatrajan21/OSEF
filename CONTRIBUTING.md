# Contributing to OSEF

First off, thank you for considering contributing to OSEF! It's people like you that make open source such a fantastic community.

## ⚠️ Important Note: We are in Sprint 1
OSEF is currently entering its very first implementation sprint. 
If you are reading this, you are looking at the frozen foundational architecture. **Production coding is just beginning.**

## How Decisions Are Made
Before proposing a massive PR, please read:
1. **The Architecture:** `architectures/REFERENCE_ARCHITECTURE.md`.
2. **The Change Control Policy:** `release/CHANGE_CONTROL_POLICY.md`.

We use an **RFC (Request for Comments)** process for architectural shifts. If you want to change how the Event Bus works, submit an RFC first. If you want to fix a typo or solve an open issue on the backlog, just open a PR!

## Development Setup (Coming Soon)
Since we are in Sprint 1, the `pyproject.toml` and standard `uv` commands are actively being written. 
Check back in a few days for the exact commands to run the test suite and local environment.

## Where to Start?
1. Check the [Engineering Backlog](implementation/ENGINEERING_BACKLOG.md).
2. Look for issues labeled `good first issue` or `help wanted` on GitHub.
3. Drop into our [Discussions](COMMUNITY.md) and say hi!

## Code Review Expectations
- All PRs must pass `mypy --strict`.
- All PRs must maintain test coverage and pass `ruff` formatting.
- Follow the guidelines in the [Coding Standards](implementation/CODING_STANDARDS.md).

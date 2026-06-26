# Contributing to OSEF

First off, thank you for considering contributing to OSEF! It's people like you that make open source such a fantastic community.

## ⚠️ Important Note: Our Engineering Philosophy
OSEF is not a typical open-source project. We operate under strict enterprise governance and adhere to an immutable set of engineering heuristics.
Before you write any code or submit a PR, you **must** read and understand:
1. **[The OSEF Constitution](governance/CONSTITUTION.md)**
2. **[The Engineering Principles](governance/ENGINEERING_PRINCIPLES.md)**

If a Pull Request violates these principles, it will be rejected.

## How Decisions Are Made

We use an **RFC (Request for Comments)** process for all architectural shifts. 
- **Want to fix a bug or add a minor feature?** Open an Issue using our templates, then open a Pull Request.
- **Want to change how a core component works?** Submit an RFC Proposal Issue first. Do not write code until the RFC is accepted.

## Development Setup

We recommend using `uv` for dependency management, though `pip` works fine.

```bash
# Clone the repository
git clone https://github.com/Aryamannatrajan21/OSEF.git
cd OSEF

# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,docs]"
```

## Code Review Expectations

All code must pass our strict CI pipeline before merging:
- **Linting:** Must pass `ruff check .` and `ruff format --check .`
- **Type Checking:** Must pass `mypy src/` strictly.
- **Tests:** Must pass the `pytest` suite on all supported Python versions.
- **Reviews:** Requires at least one approval from a designated `CODEOWNER`.

## Where to Start?

1. Check the [Engineering Backlog](implementation/ENGINEERING_BACKLOG.md) to see what we are currently working on. (We are currently in **Sprint 2: Transformation Engine**).
2. Look for issues labeled `good first issue` or `help wanted`.
3. Drop into our [GitHub Discussions](https://github.com/Aryamannatrajan21/OSEF/discussions) and say hi!

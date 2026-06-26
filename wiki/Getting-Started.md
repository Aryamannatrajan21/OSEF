# Getting Started with OSEF

Welcome to the OSEF engineering team! This guide will walk you through setting up your environment so you can start analyzing repositories and contributing to the framework.

## 1. Prerequisites
- **Python**: `3.12` or `3.13`
- **Git**: Latest version
- **uv** *(Recommended)*: Our preferred lightning-fast Python package manager.

## 2. Installing OSEF
To install OSEF globally to use the CLI on your local repositories:
```bash
pip install git+https://github.com/Aryamannatrajan21/OSEF.git
```

## 3. Development Environment
If you want to contribute to OSEF itself, follow these steps:

### Repository Setup
```bash
git clone https://github.com/Aryamannatrajan21/OSEF.git
cd OSEF
```

### Virtual Environment
We recommend using `uv`:
```bash
uv venv
source .venv/bin/activate
uv pip install -e ".[dev,docs]"
```

## 4. Running the Checks
Before committing any code, ensure you pass our strict CI checks.

**Tests:**
```bash
pytest tests/ --cov=src
```

**Linting & Formatting:**
```bash
ruff check .
ruff format --check .
```

**Type Checking:**
```bash
mypy src/
```

## 5. Building Documentation
We use MkDocs Material. To serve the docs locally:
```bash
mkdocs serve
```

## 6. Repository Tour
- `src/osef/`: The core framework (Scanner, Parser, EKG, Transformation Engine).
- `tests/`: Our comprehensive `pytest` test suite.
- `plugins/`: Official and community-contributed plugins.
- `governance/`: The Constitution, Engineering Principles, and Manifesto.
- `architectures/`: All canonical RFCs and ADRs.

---
*Last Updated: Phase II | Related Docs: [CONTRIBUTING.md](../CONTRIBUTING.md)*

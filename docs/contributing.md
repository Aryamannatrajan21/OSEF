# Contributing to OSEF

We welcome contributions from hackers, compiler engineers, and tool builders. This document outlines our development workflows, coding standards, and verification invariants.

---

## 1. Development Setup

1. Fork and clone the repository.
2. Create an isolated Python 3.12+ virtual environment:
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies in editable mode:
   ```bash
   pip install --upgrade pip
   pip install -e ".[dev,docs,ui]"
   ```

---

## 2. Coding Standards & Invariants

* **Tone**: Strictly professional, developer-to-developer communication. Zero marketing hype or AI buzzwords.
* **Formatting & Linting**: We enforce strict code formatting via `ruff`. You MUST run linting before committing:
  ```bash
  ruff format .
  ruff check .
  ```
* **Type Checking**: All core Python code must pass static type checking:
  ```bash
  mypy src/
  ```
* **Testing**: All new features or architectural rules must include automated test coverage:
  ```bash
  pytest tests/ --cov=src
  ```

---

## 3. Pull Request Process

1. Create a feature branch from `main` (`git checkout -b feat/my-feature`).
2. Implement your changes and verify against existing benchmark fixtures.
3. Ensure all CI checks (Ruff, MyPy, Pytest, MkDocs) pass locally.
4. Submit your pull request with an objective verification plan.
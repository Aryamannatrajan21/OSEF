# Playbook: Modern Python Library

## Objective
Build a robust, well-tested Python library that conforms to OSEF standards and is ready for PyPI publication.

## 1. Initialization
Start by scaffolding the project:
```bash
osef scaffold library --lang python
```
*What happens:* OSEF generates `pyproject.toml` (configured for `uv` or `hatchling`), standard `tests/`, and sets up `ruff` for linting and formatting.

## 2. Setting the Context
Define your architectural intent. Run:
```bash
osef init
```
Select "Python Library" when prompted. This ensures `osef analyze` applies the correct EKK ruleset (e.g., enforcing type hints, requiring a `LICENSE`).

## 3. Writing Code and Testing
Use your standard workflow (`pytest`, `ruff`). As you code, periodically run:
```bash
osef analyze
```
OSEF will warn you if your public API lacks docstrings or if you have introduced circular dependencies.

## 4. Documentation
A library lives and dies by its documentation.
```bash
osef repair --category documentation
```
OSEF will interactively help you generate a `README.md` template, `CONTRIBUTING.md`, and configure MkDocs.

## 5. Certification
Before publishing, ensure you meet the baseline:
```bash
osef certify
```
If you pass, add the generated badge to your README.

## 6. Next Steps
See the [Release Process Playbook](release_process.md) to automate publishing to PyPI via GitHub Actions.

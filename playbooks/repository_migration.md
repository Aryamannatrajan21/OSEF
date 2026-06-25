# Playbook: Repository Migration

## Objective
Migrate an existing, disorganized repository into an OSEF-compliant structure without breaking functionality.

## 1. The Baseline Audit
Run a dry-run analysis to see the extent of the architectural debt.
```bash
osef analyze --strict
```
Expect a low score. Do not panic.

## 2. Incremental Repair: Configuration
Start by standardizing the build tools. If you use `setup.py`, OSEF will recommend migrating to `pyproject.toml`.
```bash
osef repair --category packaging
```
OSEF generates the `pyproject.toml` based on your existing requirements. *Manual verification is required here.*

## 3. Incremental Repair: Governance
Generate missing community files.
```bash
osef repair --category governance
```
Add a License, Code of Conduct, and PR templates.

## 4. Enforcing the Standard
Once the repository hits an acceptable baseline, lock it in by adding OSEF to your CI pipeline. See the [GitHub Actions Playbook](github_actions.md).

## 5. Long-Term Refactoring
Use `osef map` to find dependency cycles in the source code. Refactor these slowly, using `osef analyze` after each commit to ensure the architecture is improving.

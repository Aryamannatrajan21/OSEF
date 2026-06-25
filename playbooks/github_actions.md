# Playbook: GitHub Actions Integration

## Objective
Automate OSEF checks in CI to enforce architectural standards on every Pull Request.

## 1. Generating the Workflow
Run the interactive generator:
```bash
osef repair --category ci
```
Select "GitHub Actions". OSEF will generate `.github/workflows/osef-audit.yml`.

## 2. Understanding the Workflow
The generated workflow performs the following:
1. Checks out the repository.
2. Installs `uv` and Python.
3. Installs `osef` and any required plugins specified in `pyproject.toml`.
4. Runs `osef analyze --ci --fail-on-warnings`.

## 3. Non-Interactive Constraints
Because the `--ci` flag is passed, OSEF will not prompt for input. If a rule fails (e.g., a contributor forgot to update the CHANGELOG), the CLI outputs a detailed error message and exits with code `1`, failing the PR check.

## 4. Auto-Formatting (Optional)
If you trust OSEF to fix basic errors (like generating missing template files), you can configure an Action to run `osef repair --force` and push a commit back to the PR branch. *This is recommended only for advanced teams.*

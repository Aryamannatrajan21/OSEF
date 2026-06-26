# Troubleshooting

Common issues and how to resolve them when working with OSEF locally.

## Installation & Environment

### `uv` or `pip` installation fails
- Ensure you are running Python 3.12 or 3.13.
- Verify your environment is activated before installing: `source .venv/bin/activate`.

## Documentation (MkDocs)

### `mkdocs serve` fails to start
- Ensure you installed the documentation extras: `pip install -e ".[docs]"`.
- Check if port `8000` is already in use by another application.

## CI & Testing

### Tests fail locally but pass in CI (or vice versa)
- Run `pytest --cov=src` locally to ensure you didn't miss a branch.
- Ensure you are not relying on system-level packages that are missing in the GitHub Actions Ubuntu runner.

### `ruff` formatting fails the CI
- Always run `ruff format .` locally before pushing your commit. Our CI runs with `--check` and will reject unformatted code.

### MyPy complains about missing stubs
- OSEF is strictly typed. If you import a third-party library without types, you must add a `# type: ignore` comment or install the corresponding `types-*` package.

---
*Last Updated: Phase II | Related Docs: [SUPPORT.md](../SUPPORT.md)*

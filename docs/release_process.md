# OSEF Release Process

This document outlines the deterministic procedures for packaging, certifying, and publishing releases across PyPI, Docker Hub, the VS Code Marketplace, and the OSEF Plugin Marketplace.

---

## 1. Pre-Release Verification Gate

Before initiating a release, maintainers must verify that the codebase passes all E2E architectural verification gates:
```bash
# 1. Formatting & static analysis
ruff check . && ruff format --check .
mypy src/

# 2. Test suite & coverage
pytest tests/

# 3. EKG graph construction & integrity check
osef scan . --format json --output .osef/
osef validate repository .

# 4. Constitutional EPE check
osef policy check . --ci
```

---

## 2. Version Bump & Changelog

1. Update version strings in `pyproject.toml` and `vscode-extension/package.json`.
2. Generate changelog notes referencing closed PRs and architectural RFCs.
3. Commit version bump:
   ```bash
   git commit -m "chore(release): prepare v1.0.0"
   git tag -s v1.0.0 -m "Release v1.0.0"
   git push origin main --tags
   ```

---

## 3. Automated Release Pipelines

When a release tag is pushed to `main`, GitHub Actions workflows automatically:
1. **PyPI Package**: Build and publish universal Python wheels via `release.yml`.
2. **Docker Image**: Build and push multi-stage OCI containers (`osef:latest` and `osef:1.0.0`).
3. **Plugin Marketplace**: Cryptographically sign reference plugins (`publish-plugins.yml`) and update `marketplace-index.json`.
4. **VS Code Extension**: Package `.vsix` bundles for GitHub Releases and publish to Visual Studio Code Marketplace via `vsce publish`.
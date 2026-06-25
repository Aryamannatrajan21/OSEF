# OSEF Release Strategy

## Overview
Releases must be fully automated, heavily tested, and deterministically reproducible.

## 1. Versioning
We use strict Semantic Versioning (`MAJOR.MINOR.PATCH`).

## 2. Branching Model
- `main`: The stable branch. All commits here must have passed CI.
- Feature branches (`feat/*`, `fix/*`): Merged into `main` via PR.
- Release branches (`release/vX.Y.Z`): Cut from `main` to finalize a release.

## 3. Changelog Policy
All commits to `main` must follow Conventional Commits (e.g., `feat:`, `fix:`, `docs:`). 
During the release phase, the `CHANGELOG.md` is automatically generated from these commit messages.

## 4. CI/CD Publishing Pipeline (GitHub Actions)
When an annotated tag (e.g., `v1.2.0`) is pushed:
1. **Test Matrix:** `pytest` runs across Ubuntu, macOS, and Windows on Python 3.13+.
2. **Build:** `uv build` compiles the sdist and wheel.
3. **Publish:** The wheel is pushed to PyPI via Trusted Publishing (OIDC), removing the need for long-lived API tokens.
4. **Release Notes:** A GitHub Release is drafted with the auto-generated changelog.
5. **Documentation:** The `docs/` and `architectures/` are compiled via MkDocs and deployed to GitHub Pages.

## 5. Deprecation and Migration
When a feature is removed in a MAJOR release, the Release Notes MUST include a link to a specific `migration_guides/` document explaining exactly how users and plugin authors should update their code.

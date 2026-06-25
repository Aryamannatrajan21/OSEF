# Playbook: Release Process

## Objective
Automate the versioning, tagging, changelog generation, and PyPI publishing process.

## 1. Prerequisites
Ensure you use Conventional Commits (e.g., `feat: added XYZ`, `fix: resolved ABC`). OSEF relies on these to generate accurate changelogs.

## 2. The Release Command
When you are ready to cut a new version, run:
```bash
osef release prepare --bump minor
```
*What happens:*
- OSEF updates the version string in `pyproject.toml`.
- Parses git history to generate a new section in `CHANGELOG.md`.
- Commits the changes (`chore: release v1.2.0`).
- Creates an annotated Git tag (`v1.2.0`).

## 3. Pre-Release Audit
Before pushing the tag, ensure the code is production-ready.
```bash
osef certify
```
If this fails, abort the release.

## 4. Publishing
Push the tag to GitHub:
```bash
git push --tags
```
If you followed the [GitHub Actions Playbook](github_actions.md), this tag push will trigger a workflow that builds the wheel via `uv build` and publishes to PyPI using Trusted Publishing.

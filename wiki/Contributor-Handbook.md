# Contributor Handbook

Welcome to the inner workings of the OSEF project. This handbook is meant for ongoing contributors and maintainers.

## Repository Standards
- **Code Quality**: All code must strictly adhere to the PEP 8 standard, enforced via `ruff`.
- **Type Safety**: The repository is `100%` strictly typed with `mypy`. We do not accept PRs that introduce `Any` unnecessarily.
- **Security**: Security is paramount. Do not merge PRs with failing CodeQL checks. Avoid executing unsafe or untrusted AST nodes.

## Review Expectations
As a maintainer or reviewer:
1. Validate that the PR does not bypass the Engineering Knowledge Graph.
2. Ensure tests cover both edge cases and happy paths.
3. Check the PR description: Does it answer *why* the change was made?
4. If the PR alters architecture, ensure it links to an approved ADR.

## Release Workflow
We follow Semantic Versioning.
1. Draft release notes locally.
2. A maintainer tags a release `vX.Y.Z`.
3. The GitHub Actions release pipeline builds the `.whl` and `.tar.gz` and pushes to PyPI.

## Mentorship
We actively encourage senior engineers to mentor newcomers. If you see a `help wanted` issue, consider guiding a new contributor through the process in the Discussions tab.

---
*Last Updated: Phase II | Related Docs: [COMMUNITY.md](../COMMUNITY.md)*

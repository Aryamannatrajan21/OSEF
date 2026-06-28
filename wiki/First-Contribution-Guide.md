# First Contribution Guide

We hold OSEF to an enterprise-grade standard. Whether you are fixing a typo or designing a new subsystem, this guide ensures your contribution is merged smoothly.

## 1. The Workflow
We strictly use the **Fork and Pull Request** workflow.
1. Fork the OSEF repository.
2. Clone your fork locally.
3. Add the `upstream` remote.

## 2. Branch Naming
Please use semantic branch names:
- `feat/add-python-parser`
- `fix/ekg-caching-bug`
- `docs/update-readme`
- `chore/update-dependencies`

## 3. Coding Standards
Read the [Engineering Philosophy](Engineering-Philosophy). 
- All code must be strictly typed (`mypy --strict`).
- All functions must have clear docstrings.
- Ensure test coverage remains above our strict thresholds.

## 4. Commit Messages
We use Conventional Commits.
- `feat: added caching to EKG`
- `fix: resolved circular dependency in parser`
- `docs: updated first contribution guide`

## 5. Submitting a Pull Request
1. Open a PR against the `main` branch.
2. Fill out the **Pull Request Template** completely.
3. Ensure all automated GitHub Actions (Ruff, MyPy, PyTest, CodeQL) pass.

## 6. Review Process & CODEOWNERS
We have a strict `CODEOWNERS` policy. Direct pushes to `main` are disabled.
Your PR must receive at least **one approving review** from the designated maintainer of the subsystem you are modifying.

## 7. Major Changes (RFCs and ADRs)
If you want to make a structural or architectural change, **do not write code first**.
1. Submit an **RFC (Request for Comments)** Issue.
2. Discuss the architecture with maintainers.
3. Once the RFC is approved, an **ADR (Architecture Decision Record)** will be drafted.
4. Only then should you begin implementation.

---
*Last Updated: v1.0.0-LTS | Related Docs: [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md)*

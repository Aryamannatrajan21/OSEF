# Playbook: Community Growth

## Objective
Transform an open-source repository from a solo-developer project into a welcoming, sustainable community project.

## 1. The Welcome Mat
Contributors judge a project by its README.
```bash
osef repair --rule docs-readme-standard
```
Ensure your README answers: What does it do? How do I install it? How do I use it?

## 2. Clear Contribution Pathways
Potential contributors need to know how to set up the development environment.
```bash
osef repair --category community
```
This generates:
- `CONTRIBUTING.md`: Detailing the `uv` setup, testing commands, and PR process.
- `CODE_OF_CONDUCT.md`: Ensuring a safe environment.
- Issue Templates: So bugs are reported with reproducible steps, not just "it broke."

## 3. Recognizing Contributors
Automate the acknowledgment of people who help. Integrate the `allcontributors` bot into your README, or use OSEF to scan git history and generate an `AUTHORS.md` file automatically.
```bash
osef generate authors
```

## 4. Managing Stale Issues
As the project grows, issues will pile up. OSEF can help configure GitHub Actions to automatically label and close stale issues, keeping the backlog manageable and your cognitive load low.

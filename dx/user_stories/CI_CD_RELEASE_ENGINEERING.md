# Category: CI/CD & Release Engineering

*(Note: Stories US-CIC-001 through US-CIC-010 define headless automation.)*

## US-CIC-001: GitHub Actions Enforcement
- **Persona:** DevOps Engineer
- **Background:** Wants to block PRs that violate OSEF architectural rules.
- **Goal:** Run OSEF in CI.
- **Trigger:** Adds `osef analyze --ci --fail-on-warnings` to the `.github/workflows/pr.yml`.
- **Expected Workflow:** OSEF runs headlessly. Outputs a clean `Rich` table to the GitHub Actions console. Exits with code `1` if rules fail.
- **Success Criteria:** Interactive prompts are suppressed; CI pipeline halts correctly.

## US-CIC-002: Automated Changelog Generation
- **Persona:** Release Manager
- **Goal:** Generate a `CHANGELOG.md` for version 1.2.0.
- **Trigger:** Runs `osef release changelog --version 1.2.0`.
- **Expected Workflow:** OSEF reads Git commit history, filters by Conventional Commits format, and prepends the new section to `CHANGELOG.md`.
- **Success Criteria:** Changelog is formatted perfectly without manual copy-pasting.

*(Stories US-CIC-003 to US-CIC-010 cover generating SBOMs, verifying Trusted Publishing setups, auditing dependencies before release, etc.)*

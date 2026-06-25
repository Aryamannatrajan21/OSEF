# Category: Team Collaboration

*(Note: Stories US-COL-001 through US-COL-010 define multi-developer workflows.)*

## US-COL-001: Sharing Project Configuration
- **Persona:** Tech Lead
- **Background:** Configured OSEF to be extremely strict for a new microservice.
- **Goal:** Ensure all other developers use the same strictness.
- **Trigger:** Edits `pyproject.toml` to add `[tool.osef] strictness = "high"`. Commits the file.
- **Expected Workflow:** When Junior Dev pulls the repo and runs `osef analyze`, OSEF automatically reads the committed config.
- **Success Criteria:** Configuration is perfectly portable.

## US-COL-002: Resolving Rule Conflicts
- **Persona:** Senior Developer
- **Goal:** Disagree with an OSEF rule regarding file length, wants to suppress it.
- **Trigger:** Adds a comment `# osef:disable-next-line(arch-005)` in the code, or adds an exclusion to `pyproject.toml`.
- **Expected Workflow:** OSEF ignores the violation during the next `osef analyze`.
- **Success Criteria:** The team can override the framework when necessary.

*(Stories US-COL-003 to US-COL-010 cover onboarding new devs via OSEF, standardizing PR comments, synchronizing EKK rule versions, etc.)*

# Category: Repository Governance

*(Note: Stories US-GOV-001 through US-GOV-012 define how teams maintain long-term repository health.)*

## US-GOV-001: Drafting an ADR
- **Persona:** Lead Architect
- **Background:** Decided to switch from SQLite to PostgreSQL.
- **Goal:** Document the decision using standard Architectural Decision Records.
- **Trigger:** Runs `osef adr new "Switch to PostgreSQL"`.
- **Expected Workflow:** OSEF generates `docs/architecture/adr/0004-switch-to-postgresql.md` with standard boilerplate (Context, Decision, Consequences).
- **Success Criteria:** ADR is formatted correctly and tracked by `osef analyze`.

## US-GOV-002: Enforcing Code of Conduct
- **Persona:** Community Manager
- **Goal:** Ensure a standard Contributor Covenant is in place.
- **Trigger:** Runs `osef repair --rule gov-002`.
- **Expected Workflow:** OSEF interactively asks for the community email address, then generates the `CODE_OF_CONDUCT.md`.
- **Success Criteria:** The file matches the latest Contributor Covenant standard.

*(Stories US-GOV-003 to US-GOV-012 cover managing stale issues, standardizing PR reviews, automating changelog generation, etc.)*

# Category: Installation & Onboarding

*(Note: Stories US-INO-001 through US-INO-010 define the first-touch experience.)*

## US-INO-001: The Global Install
- **Persona:** Weekend Developer
- **Background:** Uses `uv` for Python tooling.
- **Goal:** Install OSEF cleanly without polluting system Python.
- **Trigger:** Runs `uv tool install osef`.
- **Expected Workflow:** Installation takes < 5 seconds. `osef --version` returns immediately.
- **Success Criteria:** Installed globally.

## US-INO-002: The Interactive First Run
- **Persona:** First-time User
- **Goal:** Configure OSEF telemetry and cache settings.
- **Trigger:** Runs `osef` with no arguments.
- **Expected Workflow:** OSEF detects a missing `~/.osef/osef.yaml` and launches a 2-question interactive wizard.
- **Success Criteria:** Global config is saved. Help menu is displayed.

*(Stories US-INO-003 to US-INO-010 cover CI/CD headless installation, air-gapped installation, plugin auto-discovery during boot, etc.)*

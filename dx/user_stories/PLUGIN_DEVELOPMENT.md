# Category: Plugin Development

*(Note: Stories US-PLG-001 through US-PLG-010 define the extension ecosystem.)*

## US-PLG-001: Scaffolding a Custom Plugin
- **Persona:** Corporate Platform Engineer
- **Background:** Needs OSEF to enforce internal company naming conventions.
- **Goal:** Create a private OSEF plugin.
- **Trigger:** Runs `osef plugin create "Acme Corp Linter"`.
- **Expected Workflow:** A new directory is created with a `BasePlugin` subclass and a dummy EKK rule JSON file.
- **Success Criteria:** The generated plugin can be installed locally via `pip install -e .` and immediately shows up in `osef plugins list`.

## US-PLG-002: Unit Testing a Plugin
- **Persona:** Open Source Contributor
- **Goal:** Verify that their new `osef-django` plugin correctly identifies missing CSRF middleware.
- **Trigger:** Runs `pytest`.
- **Expected Workflow:** Uses `from osef.testing import TestCore` to pass a mocked Django project structure into their plugin logic.
- **Success Criteria:** Tests run in < 1 second without hitting the filesystem or network.

*(Stories US-PLG-003 to US-PLG-010 cover publishing plugins, injecting CLI commands, appending to the EKK, overriding Core rules, etc.)*

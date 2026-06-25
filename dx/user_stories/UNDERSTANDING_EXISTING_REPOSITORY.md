# Category: Understanding an Existing Repository

*(Note: Stories US-UND-001 through US-UND-010 define how developers map unfamiliar codebases.)*

## US-UND-001: The AI Context Export
- **Persona:** Freelance Developer
- **Background:** Inherited a 5-year-old undocumented Django project. Wants to use Cursor to fix bugs.
- **Goal:** Give Cursor the project's architectural context.
- **Trigger:** Runs `osef export-context --target cursor`.
- **Expected Workflow:** OSEF scans the repo, determines it is Django, extracts relevant EKK rules, and writes a `.cursorrules` file.
- **Success Criteria:** Cursor's AI now writes code adhering to the project's implied standards.

## US-UND-002: Generating the Architecture Map
- **Persona:** New Hire
- **Background:** Lost in a sea of microservices.
- **Goal:** Understand module dependencies.
- **Trigger:** Runs `osef map`.
- **Expected Workflow:** OSEF generates a Mermaid.js dependency graph artifact and saves it to `docs/architecture/MAP.md`.
- **Success Criteria:** The graph accurately reflects Python module imports.

*(Stories US-UND-003 to US-UND-010 cover finding dead code, mapping API endpoints, identifying testing gaps, etc.)*

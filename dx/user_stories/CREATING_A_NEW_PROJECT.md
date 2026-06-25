# Category: Creating a New Project

*(Note: Stories US-NEW-001 through US-NEW-010 define greenfield project scaffolding.)*

## US-NEW-001: The Python Library Skeleton
- **Persona:** Open Source Author
- **Background:** Wants to write a new Python library but hates copying boilerplate.
- **Goal:** Generate a standard, secure project structure.
- **Trigger:** Runs `osef scaffold library --lang python`.
- **Expected Workflow:** 
  1. OSEF asks for the project name and author.
  2. Generates `pyproject.toml` (uv/hatchling), `tests/`, `.github/workflows/`, and `README.md`.
  3. Initializes git.
- **Success Criteria:** A passing `pytest` suite exists out of the box.

## US-NEW-002: Licensing the Greenfield
- **Persona:** Junior Developer
- **Background:** Doesn't know the difference between MIT and GPL.
- **Goal:** Pick a license safely.
- **Trigger:** Runs `osef repair --category governance`.
- **Expected Workflow:** OSEF asks "Do you want to require downstream users to open-source their changes?" and recommends MIT or GPL based on the answer.
- **Success Criteria:** `LICENSE` file is generated.

*(Stories US-NEW-003 to US-NEW-010 cover adding CI templates, setting up pre-commit hooks, generating PR templates, etc.)*

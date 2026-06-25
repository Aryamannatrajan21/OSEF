# Category: Open Source Transformation

*(Note: Stories US-OST-001 through US-OST-012 define the core OSTE engine workflow.)*

## US-OST-001: The First Audit
- **Persona:** Solo Founder
- **Background:** Has a working SaaS, wants to open-source the core logic.
- **Goal:** Know what's missing before making the repo public.
- **Trigger:** Runs `osef analyze`.
- **Expected Workflow:** 
  1. OSEF parses files without internet access.
  2. Outputs a table: Missing `SECURITY.md`, missing `CONTRIBUTING.md`, hardcoded secrets detected in `tests/`.
- **Success Criteria:** Developer has an actionable checklist.

## US-OST-002: Interactive Certification
- **Persona:** Open Source Maintainer
- **Goal:** Get the OSEF "Certified Open Source" badge.
- **Trigger:** Runs `osef certify`.
- **Expected Workflow:** OSEF runs the audit. Passes 18/20 rules. Fails on "No Issue Templates." Developer fixes it, re-runs, and receives the SVG badge url.
- **Success Criteria:** Certification score is deterministically reproducible.

*(Stories US-OST-003 to US-OST-012 cover auditing secrets, verifying CI/CD parity, enforcing changelog standards, repairing missing licenses, etc.)*

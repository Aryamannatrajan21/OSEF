# Category: Discovering OSEF

*(Note: Stories US-DIS-001 through US-DIS-010 define the pre-installation and evaluation phases of OSEF.)*

## US-DIS-001: The "What is this?" Evaluation
- **Persona:** Senior Open Source Maintainer
- **Background:** Reads about OSEF on HackerNews.
- **Goal:** Understand if OSEF is a linter, a generator, or something else without installing it.
- **Trigger:** Visits the OSEF documentation website.
- **Expected Workflow:** 
  1. Lands on the homepage.
  2. Reads the "OSEF is an Engineering OS, not a linter" manifesto.
  3. Views a 30-second animated terminal SVG of `osef analyze`.
- **Success Criteria:** Understands that OSEF checks architectural intent, not just formatting.
- **Related Capabilities:** Documentation, Website.

## US-DIS-002: Exploring the Ruleset
- **Persona:** Security Researcher
- **Background:** Skeptical of AI tools. Wants to know what "rules" OSEF actually enforces.
- **Goal:** Browse the EKK online.
- **Trigger:** Clicks "Browse Rules" on the website.
- **Expected Workflow:** Navigates a web-based, tagged view of the EKK. Filters by `language:python` and `domain:security`.
- **Success Criteria:** Finds the rule requiring `bandit` in CI and trusts the system's rigor.

*(Stories US-DIS-003 to US-DIS-010 follow similar structures exploring plugin discovery, offline constraints, AI integrations, etc.)*

# Category: Enterprise & Future Workflows

*(Note: Stories US-ENT-001 through US-ENT-010 define edge cases, scale, and future vision.)*

## US-ENT-001: The Private EKK Server
- **Persona:** Enterprise Security Architect
- **Background:** Bank regulations prohibit using public open-source rules without internal review.
- **Goal:** Host a private version of the Engineering Knowledge Kernel.
- **Trigger:** Configures `OSEF_EKK_ENDPOINT=https://internal.bank.com/ekk` in environment variables.
- **Expected Workflow:** OSEF fetches rules from the internal server instead of the public SQLite/Markdown bundle.
- **Success Criteria:** Absolute control over engineering standards.

## US-ENT-002: Multi-Repo Auditing (Monorepo)
- **Persona:** Staff Engineer
- **Goal:** Run `osef analyze` across 50 microservices in a single monorepo.
- **Trigger:** Runs `osef analyze --recursive`.
- **Expected Workflow:** OSEF parallelizes the analysis across CPU cores, aggregating the score into a single HTML or JSON report.
- **Success Criteria:** Analysis completes in under 30 seconds despite repository size.

*(Stories US-ENT-003 to US-ENT-010 cover custom LLM providers, air-gapped CI environments, compliance mapping (SOC2), cross-language polyglot analysis, etc.)*

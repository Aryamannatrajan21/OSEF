# Playbook: Security Hardening

## Objective
Audit an existing application for security misconfigurations, secrets, and architectural vulnerabilities.

## 1. Deep Security Audit
Run the analysis with the security plugin explicitly enabled:
```bash
osef analyze --plugin osef-security --strict
```

## 2. Reviewing Findings
The report will highlight architectural security flaws:
- Docker images running as `root`.
- Outdated dependencies with known CVEs (if `osef-deps` is installed).
- Missing `SECURITY.md`.
- Missing static analysis tools (like `bandit` for Python) in the CI pipeline.

## 3. Automated Remediation
For structural fixes, let OSEF repair the repository.
```bash
osef repair --category security
```
*What happens:*
- Generates a `SECURITY.md` template.
- Updates `.github/workflows/` to include automated security scanning.
- Appends standard secret-scanning exclusions to `.gitignore`.

## 4. Manual Remediation
For code-level vulnerabilities (e.g., hardcoded SQL queries), OSEF will flag the file and line number. You must refactor the logic manually to use parameterized queries or an ORM.

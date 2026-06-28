# OSEF Enterprise Security Policy

## 🛡️ Security Commitment

The Open Source Engineering Framework (OSEF) is engineered for enterprise environments where codebases are intellectual property and absolute security is non-negotiable. As an architecture intelligence framework that parses, reasons over, and transforms proprietary source code, we treat security as a foundational architectural requirement, not an afterthought.

## 📅 Supported Versions & LTS Lifecycle

OSEF follows a rigorous Long Term Support (LTS) release schedule. LTS releases receive critical security updates, dependency patches, and backported stability fixes for a minimum of **24 months** from their initial release.

| Version | Status | Release Date | End of Active Support | End of Security Support (EOL) |
| ------- | ------ | ------------ | --------------------- | ----------------------------- |
| **1.0.x (LTS)** | :white_check_mark: **Supported** | June 2026 | June 2027 | **June 2028** |
| 0.5.x-alpha | :x: Unsupported | - | - | - |
| 0.4.x-alpha | :x: Unsupported | - | - | - |
| 0.3.x-alpha | :x: Unsupported | - | - | - |
| 0.2.x-alpha | :x: Unsupported | - | - | - |
| 0.1.x-alpha | :x: Unsupported | - | - | - |

*Note: Minor version updates (e.g., 1.0.1 to 1.0.2) within an LTS branch are guaranteed to be non-breaking and solely contain security patches, dependency updates, and bug fixes.*

## 🚨 Reporting a Vulnerability

We deeply appreciate the efforts of security researchers and the community in keeping OSEF secure. **Please do not report security vulnerabilities through public GitHub issues.**

### How to Report
To ensure a responsible disclosure process, all security vulnerabilities must be reported through **GitHub Private Vulnerability Reporting**:
1. Navigate to the **[Security tab](https://github.com/Aryamannatrajan21/OSEF/security)** of this repository.
2. Click on **Advisories** in the sidebar.
3. Click **Report a vulnerability**.
4. Alternatively, you can use our [Security Report Issue Template](https://github.com/Aryamannatrajan21/OSEF/issues/new?template=security_report.md) if you are unable to use the Advisories feature, but please ensure the issue is marked as **confidential**.

### What to Include
When submitting a report, please provide:
- A detailed description of the vulnerability and its impact.
- Exact steps to reproduce the issue (including sample repositories or inputs).
- Potential impact vectors (e.g., Engineering Knowledge Graph injection, Policy Engine sandbox escapes, or AST parser memory leaks).
- Any proposed mitigations or patches, if applicable.

## ⏱️ Response Timelines & SLAs

As an enterprise LTS project, we adhere to strict Service Level Agreements (SLAs) for security responses:
- **Initial Acknowledgement**: Within **48 hours**.
- **Initial Triage & Impact Assessment**: Within **72 hours**.
- **Status Updates**: Every **7 days** during active remediation.
- **Critical CVE Patch Release**: Within **14 days** of verification.
- **High/Medium Patch Release**: Delivered in the next scheduled monthly LTS patch.

## 🔒 Supply Chain & Ecosystem Security

### Dependency Management
- OSEF rigidly pins all transitive and direct dependencies.
- Automated dependency scanning (Dependabot) and SAST analysis (CodeQL) run continuously against the `main` and LTS branches.
- Upstream CVEs in our dependency tree (such as `tree-sitter`) are evaluated within 48 hours and patched in the next minor LTS release.

### Secure Execution & Sandboxing
OSEF is designed to execute locally or in CI environments. By design:
- **Zero-Exfiltration**: The core OSEF engine makes **zero** outbound network requests to third-party APIs unless explicitly configured by the user (e.g., external LLM endpoints).
- **Execution Boundaries**: The Engineering Policy Engine evaluates rules in an isolated context. Vulnerabilities allowing arbitrary code execution (RCE) via malicious Policy payloads are treated as Critical severity.

## 🤝 Safe Harbor

We consider security research conducted in good faith to be highly beneficial to OSEF and the broader open-source community. If you conduct your research and disclosure in accordance with this policy, we will consider your activities authorized and will not initiate legal action or law enforcement investigations against you. We will work with you to understand and resolve the issue quickly and recognize your contributions publicly upon resolution.

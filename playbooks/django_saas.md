# Playbook: Open Sourcing a Django SaaS

## Objective
Prepare a proprietary or existing Django SaaS application for open-source publication, ensuring no secrets are leaked and that the architecture is understandable to new contributors.

## 1. Context and Audit
In your Django root directory, initialize OSEF:
```bash
osef init
```
Select "SaaS / Web Application" and explicitly choose "Django" as the framework.

Run a dry-run audit to see what needs fixing before going public:
```bash
osef analyze --strict
```

## 2. Secrets and Security Sweep
The most critical step before open-sourcing is ensuring no hardcoded API keys exist.
```bash
osef audit secrets --deep
```
*Note: This relies on the `osef-security` plugin.* 
Resolve any findings by moving hardcoded credentials into environment variables managed by `django-environ` or `python-decouple`.

## 3. Governance and Legal
Ensure you have the right protections.
```bash
osef repair --category governance
```
- Select an appropriate license (e.g., AGPLv3 for SaaS).
- Generate a `SECURITY.md` detailing how to report vulnerabilities privately.
- Generate a `CODE_OF_CONDUCT.md`.

## 4. Architectural Onboarding
New contributors need to understand your app's structure.
```bash
osef map --export docs/architecture/
```
This generates a Mermaid.js diagram of your Django apps and models, making it vastly easier for outsiders to understand your domain model.

## 5. CI/CD Preparation
Ensure external contributors' PRs are formatted correctly.
```bash
osef repair --category ci
```
Select "GitHub Actions" to generate workflows for `ruff`, `pytest` (with Django DB setup), and OSEF architectural enforcement.

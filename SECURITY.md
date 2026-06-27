# Security Policy

## Supported Versions

Currently, OSEF is in a **Release Candidate** state (specifically `v1.0.0-rc1`). 
While the core architecture is frozen, we do not yet recommend OSEF for production workloads until the final stable `v1.0.0`. However, we take security seriously from day one.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| 0.4.x   | :x:                |
| 0.1.x   | :x:                |

*Note: As we reach `v1.0.0`, LTS policies will be introduced.*

## Reporting a Vulnerability

If you discover a security vulnerability in OSEF (such as an issue with how we parse ASTs, local file traversal bugs, or dependency CVEs), please report it by creating a new [Security Report Issue](https://github.com/Aryamannatrajan21/OSEF/issues/new?template=security_report.md) using our template.

**What to include:**
- A detailed description of the vulnerability.
- Steps to reproduce.
- Potential impact.

**What to expect:**
- We will acknowledge receipt of your vulnerability report within 48 hours.
- We will send you regular updates about our progress.
- Upon resolution, we will publish a security advisory and credit you for the discovery.

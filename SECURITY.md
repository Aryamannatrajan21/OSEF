# Security Policy

## Supported Versions

Currently, OSEF is in **v1.0.0 LTS** (Long Term Support). 
The core architecture is frozen and OSEF is fully certified for production workloads. However, we take security seriously from day one.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| 0.4.x   | :x:                |
| 0.1.x   | :x:                |

*Note: v1.0.0 LTS policies are now fully in effect.*

## Reporting a Vulnerability

If you discover a security vulnerability in OSEF (such as an issue with how we parse ASTs, local file traversal bugs, or dependency CVEs), please report it by creating a new [Security Report Issue](https://github.com/Aryamannatrajan21/OSEF/issues/new?template=security_report.md) using our template.

**What to include:**
- A detailed description of the vulnerability.
- Steps to reproduce.
- Potential impact (especially regarding Graph queries, Policy Engine exploits, or Runtime adapter vulnerabilities).

**What to expect:**
- We will acknowledge receipt of your vulnerability report within 48 hours.
- We will send you regular updates about our progress.
- Upon resolution, we will publish a security advisory and credit you for the discovery.

# OSEF Installation & Onboarding Specification

## Overview
The installation and onboarding journey sets the tone for the entire Developer Experience. It must be fast, secure, and immediately valuable.

## 1. Prerequisites
- Python 3.13+
- `uv` or `pipx`

## 2. Installation
The recommended installation path isolates OSEF from system Python packages.
```bash
uv tool install osef
```

## 3. First Launch
Upon running `osef` for the first time, the CLI detects the absence of a global `~/.osef/` configuration directory and initiates the onboarding wizard.

```text
Welcome to OSEF: The Open Source Engineering Framework.

It looks like this is your first time running OSEF. Let's set up your environment.

? Would you like to download the latest Engineering Knowledge Kernel (EKK) ruleset? (Y/n)
? Enable anonymous telemetry to help improve OSEF? (y/N)

Configuration saved to ~/.osef/osef.yaml.
You are ready to go! Run `osef init` in a project directory to begin.
```

## 4. Project Initialization (`osef init`)
When run inside a repository, OSEF performs a quick analysis to determine the project profile (e.g., Python Library, Node SaaS).

```text
$ osef init
Analyzing repository...
Found: pyproject.toml, .git

OSEF has detected a Python project.
? Is this an Open Source Library or a proprietary SaaS? [Library/SaaS]
> Library

Generating project configuration...
Created .osef/config.yaml

OSEF is initialized. Run `osef analyze` to evaluate your repository against open-source standards.
```

## 5. First Success
The primary goal of onboarding is to drive the user to run `osef analyze` and receive their first actionable Engineering Report within 2 minutes of installation.

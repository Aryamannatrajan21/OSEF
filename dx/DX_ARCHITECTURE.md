# OSEF Developer Experience Architecture

## Overview
Developer Experience is an architectural layer that sits directly on top of the Public API. It bridges the gap between raw system capabilities (Service Contracts) and human understanding.

## 1. Presentation Layer Architecture

### The CLI Engine
The CLI is built using `Typer` and `Rich`. It is responsible for:
- Translating exceptions into [educational error messages](ERROR_RECOVERY_GUIDELINES.md).
- Rendering [interactive workflows](INTERACTIVE_WORKFLOW_SPECIFICATION.md) using `questionary` or `Rich` prompts.
- Displaying spinners and progress bars during asynchronous OSTE operations.

### The SDK Facade
The SDK (`osef/__init__.py`) provides a facade pattern over the internal Dependency Injector, ensuring that developers opening Python shells or scripts have immediate, type-hinted access to core providers without needing to understand the underlying framework topology.

## 2. Contextual Empathy Architecture
OSEF uses the `ProjectContext` to automatically adjust its UX.
- **Example:** If `osef audit` detects a `package.json`, the presentation layer automatically highlights NPM-specific security rules from the EKK, filtering out irrelevant Python noise.

## 3. The Hook Ecosystem
The Event Bus drives the DX of Plugins.
- When `PluginRegistered` fires, the presentation layer dynamically injects the plugin's commands into the `--help` menu, categorizing them under `[Plugin: name]` headers to maintain transparency.

## 4. Telemetry and Analytics (Opt-In)
To continually improve the DX, OSEF architecture supports local telemetry (e.g., command execution times, encountered exceptions) written to `.osef/logs/`.
- No data is sent over the network unless the user explicitly opts into `osef telemetry enable`.

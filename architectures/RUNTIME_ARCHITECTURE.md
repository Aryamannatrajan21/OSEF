# OSEF Runtime Architecture

## Overview
This document specifies the lifecycle of an OSEF execution session from CLI invocation to shutdown. It defines how components are instantiated, how the Dependency Injection (DI) container is populated, and how the Event Bus manages asynchronous teardown.

## 1. Execution Lifecycle Phases

### Phase 1: Bootstrapping
1. **Invocation:** The user executes an `osef` command via the CLI (`Typer`).
2. **Configuration Loading:** The `ConfigurationProvider` reads the local `pyproject.toml`, global `osef.yaml`, and Environment Variables.
3. **DI Container Initialization:** The core injects minimal dependencies based on the configuration.

### Phase 2: Lazy Initialization
1. **Plugin Discovery:** The `PluginProvider` scans for installed `osef-*` packages.
2. **Hook Registration:** Discovered plugins register their hooks with the `EventBusProvider`.
3. **EKK Mount:** The `KnowledgeProvider` validates and mounts the storage backend (`sqlite3` MVP). Note: Data is not loaded into memory until requested.

### Phase 3: Workflow Execution (OSTE)
1. **Context Resolution:** The Transformation Engine establishes the context of the user's current directory (e.g., detecting if it is a Python or Node project).
2. **Workflow Invocation:** The specific command logic executes (e.g., `certify`).
3. **Agent Delegation:** If reasoning is required, OSTE invokes the `AgentProvider`, passing the prompt and context.

### Phase 4: Teardown
1. **Event Flushing:** The Event Bus ensures all pending Low-Priority events (like Telemetry or caching) are flushed.
2. **Resource Release:** Database connections are closed.
3. **Exit:** A determinist status code is returned to the OS.

## 2. Concurrency Model
- The runtime uses `asyncio` natively.
- Top-level `Typer` commands wrap synchronous entries into an `asyncio.run()` event loop.
- File I/O (Repository Analysis) utilizes `aiofiles` or `asyncio.to_thread` to prevent blocking the Event Bus.

## 3. Sandboxing
- The MVP operates in a local trust model. OSEF assumes the user's repository code is untrusted and will strictly perform static analysis (parsing files, reading ASTs).
- Execution of user test suites or build scripts happens exclusively via explicit prompts and standard subprocess boundaries.

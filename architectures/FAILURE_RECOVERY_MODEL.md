# OSEF Failure Recovery Model

## Overview
OSEF must be highly reliable. This specification defines how the framework handles expected and unexpected failures, prioritizing graceful degradation over hard crashes.

## 1. Exception Hierarchy
All OSEF-specific exceptions inherit from a base `OsefError`.
- `OsefError`
  - `ConfigurationError`: Missing `.env` or invalid `pyproject.toml`.
  - `StorageError`: Cannot access `.sqlite` EKK or file system permissions denied.
  - `PluginError`: A plugin threw an unhandled exception or failed to initialize.
  - `ValidationError`: EKK constraints failed during internal parsing.

## 2. Graceful Degradation Scenarios

### Scenario A: Plugin Initialization Failure
- **Trigger:** A third-party plugin throws `ImportError` or a runtime exception in `register_hooks`.
- **Response:** The Core DI container catches the exception, logs a warning via the internal Logger, and unloads the plugin. The core initialization continues successfully.

### Scenario B: AI Provider Timeout
- **Trigger:** `osef-openai` experiences a 504 Gateway Timeout while evaluating repository architecture.
- **Response:** The OSTE orchestration layer catches the `ProviderTimeoutError`. It defaults to a static rule-based evaluation from the EKK, warns the user that AI heuristics are disabled, and continues the evaluation.

### Scenario C: Corrupted Local EKK Cache
- **Trigger:** `SqliteKnowledgeAdapter` hits a `sqlite3.DatabaseError`.
- **Response:** The adapter deletes the local cache and triggers a synchronous rebuild of the database from the local Markdown source files before continuing the query.

## 3. Exception Groups
Because OSEF is heavily asynchronous and relies on the Event Bus, multiple plugins may fail simultaneously in response to a single event (e.g., `ProjectAnalyzed`).
- OSEF uses Python 3.11+ `ExceptionGroup` to bundle errors from concurrent `asyncio.gather` calls.
- The CLI formatters unpack the `ExceptionGroup` to show the user a consolidated list of non-fatal warnings at the end of execution.

## 4. Hard Failures
The system will immediately `sys.exit(1)` ONLY under the following conditions:
- Python version < 3.13.
- The Core DI container cannot be initialized (e.g., missing essential `pydantic` models).
- The user's target repository lacks required read/write filesystem permissions.

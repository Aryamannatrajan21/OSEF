# OSEF Python SDK User Experience Specification

## Overview
While the CLI provides the primary workflow, the Python SDK is the engine for extension, automation, and plugin development. The SDK must feel "Pythonic"—minimal, readable, strongly typed, and discoverable via IDE autocomplete.

## 1. Minimal Facade
Developers should not need to navigate complex directory structures to perform basic tasks. The `osef` root namespace should expose the most critical components.

```python
import osef
from osef.models import ProjectContext

# Initialize the framework
core = await osef.init()

# Analyze a directory
context = ProjectContext(path=".")
report = await core.analyze(context)

print(report.score)
```

## 2. Strong Typing and Autocomplete
The SDK must be fully typed using Python 3.13+ annotations.
- Avoid `Any` or `dict` for payloads. Use Pydantic models.
- Docstrings must follow the Google style guide to ensure IDEs render helpful tooltips.

## 3. Fluent API Design
Where appropriate, support method chaining for intuitive configuration.

```python
query = (
    core.knowledge
    .search(tags=["python", "security"])
    .filter_by(level="critical")
)
rules = await query.execute()
```

## 4. Stability
The Public SDK resides within `contracts/` and `interfaces/`. Breaking changes to these modules require a major version bump (Semantic Versioning). 

## 5. Exception Handling
Exceptions raised by the SDK should be specific and catchable. Avoid throwing generic `RuntimeError` or `Exception`.

```python
from osef.exceptions import ValidationError

try:
    await core.analyze(context)
except ValidationError as e:
    print(f"Validation failed: {e.details}")
```

## 6. Examples First
The documentation for the SDK should prioritize common workflows (e.g., "How to query a rule", "How to trigger an event") over internal architecture diagrams.

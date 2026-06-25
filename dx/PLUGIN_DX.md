# OSEF Plugin Developer Experience Specification

## Overview
A framework is only as strong as its ecosystem. OSEF must make plugin development frictionless. The Plugin DX prioritizes contributor happiness, minimal boilerplate, and clear upgrade paths.

## 1. Plugin Creation
Developers should not have to manually scaffold a plugin. OSEF provides a generator command:

```bash
osef plugin create "My Custom Linter"
```

This generates a complete `osef-my-custom-linter` directory containing:
- `pyproject.toml` (pre-configured for `uv`)
- A subclass of `BasePlugin`
- A test suite scaffolding
- GitHub Action workflows for testing and publishing

## 2. Registration via Entry Points
Plugins register themselves using Python packaging entry points in `pyproject.toml`. This means users simply `pip install` the plugin, and OSEF discovers it automatically on the next run. No manual configuration files required.

```toml
[project.entry-points."osef.plugins"]
my_linter = "osef_my_custom_linter.plugin:MyLinterPlugin"
```

## 3. Testing and Debugging
The SDK must provide a `TestContainer` that mocks the Event Bus and Storage adapters, allowing plugin authors to write fast, isolated `pytest` assertions.

```python
from osef.testing import TestCore

async def test_my_plugin():
    core = TestCore()
    core.register_plugin(MyLinterPlugin())
    
    # Assert event was published
    assert core.events.was_published("LintCompleted")
```

## 4. Publishing
Plugins are standard Python packages. They are published to PyPI using standard tools (`twine`, `uv build`). OSEF documentation should provide clear guides on how to use Trusted Publishing via GitHub Actions.

## 5. Compatibility and Versioning
When a Plugin is loaded, OSEF checks the required Core version specified in the plugin's metadata. If there is a major version mismatch, OSEF gracefully disables the plugin and logs a clear warning, rather than crashing the runtime.

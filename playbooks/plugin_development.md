# Playbook: Plugin Development

## Objective
Create, test, and distribute a custom OSEF plugin.

## 1. Scaffolding
Create the plugin shell:
```bash
osef plugin create "My Custom Plugin"
```
Navigate to the new directory.

## 2. Defining Hooks
Open `plugin.py`. Subclass `BasePlugin` and implement `register_hooks`.
```python
async def register_hooks(self, event_bus: EventBusProvider):
    event_bus.subscribe("ProjectAnalyzed", self.on_analyze)
```

## 3. Implementing Logic
Write your `on_analyze` handler. It receives the ASTs parsed by the core OSTE engine. Add your custom violations to the context if your rules are broken.

## 4. Local Testing
Run the generated test suite:
```bash
pytest
```
The test suite uses `TestCore` to mock the Event Bus, allowing you to trigger `ProjectAnalyzed` events programmatically and assert your plugin responds correctly.

## 5. Local Installation
Install your plugin into your local `uv` environment so the OSEF CLI can discover it.
```bash
pip install -e .
```
Verify it loads:
```bash
osef plugins list
```

## 6. Distribution
When ready, build and publish to PyPI using `uv build` and `twine`. Once published, any OSEF user can install it via:
```bash
uv tool install osef --with osef-my-custom-plugin
```

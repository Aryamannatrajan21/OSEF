# Plugin Development

OSEF's true power lies in its extensibility. The Plugin SDK allows you to hook into the Transformation Engine and the Engineering Knowledge Graph.

## Plugin Lifecycle
1. **Discovery**: OSEF scans the `plugins/` directory and installed `osef-*` packages.
2. **Registration**: Plugins register their hooks (e.g., custom parsers, validation rules).
3. **Execution**: During the EIL or Transformation phases, plugins intercept and modify data.

## Plugin Manifest
Every plugin must define a `manifest.json` (or entry in `pyproject.toml`):
```json
{
  "name": "osef-plugin-golang",
  "version": "1.0.0",
  "entry_point": "osef_plugin_golang:register"
}
```

## Best Practices
- **Never block the main thread**: Use async hooks where possible.
- **Fail gracefully**: If your parser fails on a strange syntax tree, log a warning, do not crash OSEF.
- **Version compatibility**: Always define your OSEF `>=` dependency in your manifest.

## Testing Plugins
Use the `osef.testing.PluginTestCase` to write unit tests for your plugins.

---
*Last Updated: v1.0.0-LTS | Maintainer: @Aryamannatrajan21*

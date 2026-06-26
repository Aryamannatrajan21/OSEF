# SDK Gaps Tracking

Tracks missing APIs, weaknesses, and required enhancements discovered during ecosystem validation.
*Never silently modify Core. SDK evolution must be intentional.*

| Plugin | Missing API / Gap | Reason | Temporary Workaround | Resolution Status |
| :--- | :--- | :--- | :--- | :--- |
| `osef_python` | Need `pyyaml` in Plugin `pyproject.toml` | `PluginManifest` expects data loading from YAML, but standard lib does not have a YAML parser. | Included `pyyaml` explicitly in `plugins/python/pyproject.toml`. | TBD - Should `ExtensionHost` load manifest without Plugin doing it? |
| `osef_python` | `Pipeline Engine` fires no events | `Pipeline Engine` orchestrates the build process but does not instantiate or use the `EventBus`. | The test suite will manually trigger the plugin parser alongside the core builder. | RESOLVED - Migrated to `PipelineEngine` and `EventBus` hooks |
| `osef_python` | `ExtensionContext` restricts mutation | "Never mutate the EKG from plugins" guardrail contradicts parser plugins needing to build the graph. | The plugin will generate its own isolated `KnowledgeGraph` instance for the parity test. | RESOLVED - Introduced `CapabilityRegistry` and `BaseParserProvider` |


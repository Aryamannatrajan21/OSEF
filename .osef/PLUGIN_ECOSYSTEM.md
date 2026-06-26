# OSEF Plugin Ecosystem

Tracks the status, readiness, and tiering of OSEF Plugins.

## Official Plugins (Maintained by Core)
- **`osef-parser-python`**: The default `ast` parser (Currently embedded in Core, pending full extraction to a plugin in Sprint 6).

## Reference Plugins (Maintained by Core for Demonstration)
- **`osef-plugin-example`**: *(Planned for Sprint 5)*. Will demonstrate `ExtensionContext`, `EventBus` hooks, and basic Graph Queries.
- **`osef-report-markdown`**: *(Planned)*. Will convert EPE Findings into Markdown artifacts.

## Community Plugins
*(Awaiting Marketplace Protocol implementation).*

## Compatibility Matrix
| Plugin | Required SDK Version | Status |
| :--- | :--- | :--- |
| `osef-plugin-example` | `^0.4.0` | Pending |

## Marketplace Readiness
- **Capabilities Negotiation**: Implemented.
- **Sandboxing**: Designed (See `PLUGIN_SANDBOX_SPEC.md`).
- **Distribution Protocol**: Pending cryptographic signature implementation.

# OSEF Plugin Ecosystem

Tracks the status, readiness, and tiering of OSEF Plugins.

## Official Plugins (Maintained by Core)
- **`osef-parser-python`**: The default `ast` parser (Currently embedded in Core, pending full extraction to a plugin in Sprint 6).

### `reference-plugins/`

1. **`osef-python`**
   - **Status**: Stable
   - **Type**: Parser Capability
   - **Role**: Strangler migration anchor. Provides Python AST parsing via the public SDK.

2. **`osef-documentation`**
   - **Status**: 1.0.0 (Certified)
   - **Type**: Intelligence Plugin (Graph Enrichment, Policy, Report, CLI)
   - **Role**: Discovers, parses, and enriches the EKG with documentation intelligence. Validates Capability Descriptors and `GraphDelta` transactions.

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

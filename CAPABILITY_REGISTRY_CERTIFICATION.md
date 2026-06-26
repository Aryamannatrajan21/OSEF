# Capability Registry Certification

**Status**: Certified
**Version**: 0.4.0
**Architectural Role**: Provider Resolution & Conflict Detection

## Validated Criteria
- `[x]` Maps `PluginCapabilities` to `BaseProvider` instances.
- `[x]` Matches Language precisely.
- `[x]` Prevents duplicate un-ranked providers.
- `[x]` Handles Missing Providers deterministically (Returns `None`).
- `[x]` Passed Permanent SDK Regression Suite (`tests/sdk_contracts/`).

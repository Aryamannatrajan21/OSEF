# OSEF Language Certification Specification

Every language pack MUST pass identical certification criteria to be promoted to **Tier 1 Official**. 

## 1. Compliance Categories

### A. Graph Schema Compliance
- 100% of generated nodes and edges must adhere to `Graph Schema v5.0`.
- No custom node types outside the canonical `Software.*` taxonomy unless explicitly defined as extensions.

### B. Provenance Completeness
- 100% of structural nodes must contain valid file paths and line ranges.

### C. Semantic Completeness
The plugin must demonstrate comprehensive extraction across the following vectors:
- Functions (100%)
- Classes (100%)
- Imports (100%)
- Generics (>= 95%)
- Decorators/Annotations (100%)
- Namespaces/Modules (100%)

### D. Architectural Integrations
- **Import Resolution:** Accurately maps cross-file dependencies.
- **Namespace Correctness:** Correctly nests scopes.
- **Correlation Compatibility:** Emits nodes that the Correlation Engine can link against (e.g., matching a security finding to a `Software.Function`).
- **Policy Compatibility:** Emits graphs that pass standard cross-language OSEF policies.

### E. Performance Thresholds
- Must parse and construct the GraphDelta within standard acceptable bounds (e.g., < X ms per file).

## 2. Benchmark Suites
All plugins must be tested against a frozen corpus of canonical open-source repositories defined by `benchmark.yaml` manifests.

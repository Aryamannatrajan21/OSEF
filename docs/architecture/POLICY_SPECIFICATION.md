# Policy Specification

A `PolicySet` is a configurable definition of which `RulePacks` and individual rules are active during an analysis run.

## 1. Composition
A Policy is composed of:
- Global severity overrides.
- Enabled/Disabled rule flags.
- Pack version pins (e.g., `osef-core-architecture@^1.0.0`).

## 2. Execution
The `IntelligenceLayer` instantiates the `PolicyEngine` with a specific versioned policy, ensuring reproducible engineering assessments.

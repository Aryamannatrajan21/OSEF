# Rule Pack Specification

Rules in OSEF are grouped into `RulePack`s.

## 1. Rule Pack Identity
A Rule Pack must define an `id` (e.g., `osef-core-architecture`) and a `version` (e.g., `1.0.0`).

## 2. Distribution
Rule Packs are designed to be distributed independently. Future plugin developers can publish Rule Packs to package registries (like PyPI) and load them dynamically into the `RuleRegistry`.

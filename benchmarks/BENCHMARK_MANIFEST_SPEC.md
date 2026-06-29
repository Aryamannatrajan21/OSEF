# Benchmark Manifest Specification

Every benchmark in the OSEF Benchmark Corpus must be declarative. No repository-specific logic may be hardcoded into the Benchmark Runner.

A Benchmark Manifest defines the target repository, its ecosystem, the plugins required, and the expected outcomes (certification boundaries).

## Schema

```yaml
name: string (Required)        # Canonical name of the benchmark
repository: string (Required)  # Git URL of the repository
tier: string (Required)        # tier1 | tier2 | tier3 | tier4

languages:                     # List of primary languages to analyze
  - string

profiles:                      # High-level architecture profiles (e.g. backend, frontend)
  - string

plugins:                       # OSEF Knowledge Domains/Plugins to activate
  - string

expected:                      # The bounds defining a successful run
  minimum_nodes: integer
  minimum_edges: integer
  engineering_confidence: integer (0-100)

certification:                 # Which subsystems must certify success
  parser: boolean
  graph: boolean
  reasoning: boolean
```

## Example Manifest (`benchmarks/official/tier1/fastapi.yaml`)

```yaml
name: fastapi
repository: https://github.com/fastapi/fastapi

tier: tier1

languages:
  - python

profiles:
  - backend

plugins:
  - python
  - architecture
  - security

expected:
  minimum_nodes: 1000
  minimum_edges: 5000
  engineering_confidence: 95

certification:
  parser: true
  graph: true
  reasoning: true
```

## Manifest Rules

1. **Immutability:** Once a manifest is added to the `official/` directory, its expectations (`minimum_nodes`, `minimum_edges`) can only increase across releases unless a valid architectural reduction occurs in the target repository.
2. **Determinism:** The runner must yield the exact same graph outputs when executed multiple times against the same commit SHA defined by the manifest context.

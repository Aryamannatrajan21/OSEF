# Public Results Specification

The Benchmark Corpus is the public evidence backing every OSEF release. This document outlines how benchmark results are published and consumed by the wider ecosystem.

## The Public Benchmark Portal
For every stable release of OSEF (e.g., `v1.0.0`), a snapshot of the Benchmark Corpus results must be generated and published to the public OSEF website/portal.

## Publication Pipeline
1. **Execution:** The `BenchmarkRunner` executes the full corpus.
2. **Certification:** The `BenchmarkCertificationEngine` verifies the run.
3. **Archival:** Results are stored in `benchmarks/history/<version>/`.
4. **Generation:** The CLI command `osef benchmark dashboard` compiles the historical data into the `dashboard.json` schema.
5. **Deployment:** The CI/CD pipeline deploys the static dashboard assets to the public portal.

## Expected Public Artifacts per Project
For a project like FastAPI on OSEF v1.0.0, the public portal should make the following available:
* The Engineering Confidence Score
* Performance Metrics (Runtime, Memory)
* Graph Statistics (Nodes, Edges)
* Certification Status (Pass)
* Downloads for the raw `graph.json` and `report.md`

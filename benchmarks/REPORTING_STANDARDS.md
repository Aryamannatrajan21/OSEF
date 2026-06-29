# Benchmark Reporting Standards

Every execution of a benchmark by the `BenchmarkRunner` must produce a standardized set of artifacts. These artifacts are stored in `benchmarks/results/latest/<benchmark-name>/` and later archived in `benchmarks/history/`.

## Required Output Files

1. **`report.md`**: A human-readable summary of the benchmark run, including the status, top-level metrics, and any prominent policy violations.
2. **`report.json`**: A machine-readable compilation of all outputs for CI/CD integrations.
3. **`graph.json`**: The serialized structure of the resulting Engineering Knowledge Graph.
4. **`metrics.json`**: Raw performance metrics (runtime in ms, memory in MB, CPU utilization).
5. **`validation.json`**: The output from the `BenchmarkCertificationEngine` detailing the pass/fail status of every certification gate.
6. **`engineering_confidence.json`**: Detailed breakdown of the Engineering Confidence Score, showing how it was calculated based on resolution rates and domain coverage.
7. **`dashboard.json`**: A flattened, denormalized JSON object designed specifically to feed the Public Benchmark Dashboard.
8. **`graph.png`** (Optional): A visual rendering of the graph core structure.
9. **`architecture.png`** (Optional): A visual rendering of the extracted C4 architecture.
10. **`dashboard.png`** (Optional): A screenshot of the dashboard representation for this run.

## Consistency Rule
No field in `report.json` or `metrics.json` may be removed or renamed across minor versions. The reporting schema is part of the frozen SDK contract.

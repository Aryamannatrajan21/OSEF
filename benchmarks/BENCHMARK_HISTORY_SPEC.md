# Benchmark History Specification

Historical tracking is a core requirement of the Benchmark Corpus. Every official benchmark execution must be permanently archived to enable longitudinal regression analysis.

## Archive Structure

Benchmark results are stored in the `benchmarks/history/` directory, organized by OSEF release version, and then by the benchmark name:

```text
benchmarks/
    history/
        v1.0.0/
            fastapi/
            kubernetes/
            nextjs/
        v1.0.1/
            fastapi/
            kubernetes/
            nextjs/
```

## Immutability Rule
Once a benchmark run is archived into a versioned history folder (e.g., `v1.0.0`), it **must never be overwritten**. If a run needs to be repeated for an existing version due to a broken test, it should be appended with a timestamp or run ID, though typically historical records remain immutable.

## Tracked Metrics
The history subsystem tracks the following metrics across releases for every benchmark:
- Runtime (ms)
- Memory peak (MB)
- Graph size (Node count, Edge count)
- Engineering Confidence Score (0-100)
- Policy Findings (Violation counts)

## Usage in Certification
The `BenchmarkCertificationEngine` uses the history subsystem to detect regressions. For example, if FastAPI processing took 4.2 seconds in `v1.0.0`, an execution in `v1.0.1` that takes 8.4 seconds will trigger a performance regression failure during certification.

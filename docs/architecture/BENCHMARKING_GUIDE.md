# Benchmarking Guide

Every architectural change in OSEF must be benchmarked against a canonical corpus to ensure semantic integrity and performance.

## 1. The Corpus
The canonical benchmark corpus is located in `benchmarks/python/` and tracks high-profile open source repositories like FastAPI and Typer.

## 2. CI/CD Requirements
All Pull Requests must execute the benchmark suite to detect regressions in:
- Node discovery counts
- Edge discovery counts
- Call graph resolution depth
- Total analysis time

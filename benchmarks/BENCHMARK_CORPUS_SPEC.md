# OSEF Benchmark Corpus Specification

The Benchmark Corpus is the canonical validation platform for OSEF. It exists to continuously prove the correctness, determinism, scalability, performance, and engineering intelligence capabilities of OSEF across real-world software systems.

This document defines the canonical tiers of the corpus. No benchmark is arbitrary; each is chosen to stress a specific subsystem of the platform.

## Tier 1 — Small

**Purpose:** 
* Parser validation
* Graph generation
* Determinism
* Certification baseline
* Performance benchmarking for small codebases

**Projects:**
* FastAPI
* Flask
* Express
* Koa
* Gin
* Cobra CLI
* Picocli

---

## Tier 2 — Medium

**Purpose:**
* Architecture extraction
* Cross-module dependency graphs
* Engineering policy execution
* Basic cross-domain reasoning

**Projects:**
* NestJS
* Django
* Spring PetClinic
* Micronaut Samples
* Quarkus Quickstarts
* React
* Next.js
* Angular
* Vue

---

## Tier 3 — Large

**Purpose:**
* Graph scalability
* Correlation Engine stress-testing
* Infrastructure and Runtime mapping
* Security vulnerability blast radius calculations
* Enterprise ownership mappings

**Projects:**
* Kubernetes
* OpenTelemetry
* Apache Kafka
* Elasticsearch
* LangChain
* Apache Superset
- Airflow
* Grafana
* Prometheus

---

## Tier 4 — Massive

**Purpose:**
* Extreme scalability demonstrations
* Platform endurance and memory management tests

**Projects:**
* OpenJDK
* VS Code
* Chromium (selected components)
* Linux Kernel (selected subsystems)

---

## Benchmark Corpus Rules
1. Every project in this corpus must have a declarative YAML manifest in `benchmarks/official/`.
2. Hardcoding repository-specific logic in the Benchmark Runner is strictly forbidden.
3. Every execution of a tier must produce a deterministic report in the `benchmarks/results/latest` directory.

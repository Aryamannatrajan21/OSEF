# Correlation Engine Specification

The Correlation Engine is responsible for **Relationship Generation**. 

## Responsibility
Its sole responsibility is to execute declarative `CorrelationRules` across the Engineering Knowledge Graph (EKG) and produce `GraphDelta` instances containing **new edges** (and occasionally new nodes) that bridge isolated Knowledge Domains.

**It does NOT:**
- Execute graph traversal algorithms.
- Reason about impact, blast radius, or health.
- Emit policy findings.

## Lifecycle
1. Plugins register `CorrelationRules` in the `CorrelationRegistry`.
2. The `CorrelationEngine` iterates over these rules during the pipeline stage following Graph Enrichment.
3. Each rule evaluates the graph using `GraphQuery` and yields a `GraphDelta`.
4. The Engine merges these deltas back into the EKG.

## Example Rule Execution
A rule mapping `Software.Service` to `Infrastructure.Container` evaluates the graph, finds matching nodes, and outputs a `GraphDelta` containing `DEPLOYED_AS` edges.

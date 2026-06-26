# OSEF Architecture Evolution

Permanent record of architectural milestones and paradigms.

## 1. Foundation (v0.1.0)
- **Motivation:** Need a structural foundation for parsing logic.
- **Problem:** Fragile regex-based scripts fail on complex enterprise codebases.
- **Solution:** Implement a strict Python `ast` parser and a language-agnostic Symbol Table (Intermediate Representation).
- **Architecture Frozen:** PARSER_CONTRACT, SYMBOL_TABLE_SPEC.
- **Lessons Learned:** Extracting imports and types requires robust two-pass resolution.

## 2. Repository Intelligence (v0.2.0)
- **Motivation:** Trees are hard to query for complex semantic relationships.
- **Problem:** Determining "what calls what" or "what imports what" is computationally expensive.
- **Solution:** Introduce the **Engineering Knowledge Graph (EKG)** and Semantic Enrichment heuristics.
- **Architecture Frozen:** GRAPH_SCHEMA, SEMANTIC_MODEL.
- **Lessons Learned:** Graph abstractions natively map to architectural mental models.

## 3. Engineering Policy Engine (v0.3.0)
- **Motivation:** Imperative analyzers were becoming monolithic and hard to test.
- **Problem:** Running 50 analyzers repeats the same O(N) graph traversals 50 times.
- **Solution:** Declarative **Engineering Policy Engine (EPE)** with DAG dependency resolution and a Shared Query Cache.
- **Architecture Frozen:** EPE API, Rule Packs.
- **Lessons Learned:** Memoized graph queries are exponentially faster than imperative loops.

## 4. Engineering Platform SDK (v0.4.0)
- **Motivation:** OSEF must grow beyond its initial creators.
- **Problem:** Tightly coupled logic prevents community contributions and risks core stability.
- **Solution:** Hide internal graph mutations. Introduce the **Extension Host**, **Extension Context**, and **Event Bus**.
- **Architecture Frozen:** EPSDK, Marketplace Protocol, Sandboxing.
- **Lessons Learned:** Enforced boundary decoupling is painful but necessary for ecosystem scale.

## 5. Reference Ecosystem (Upcoming)
*(To be appended after Sprint 5).*

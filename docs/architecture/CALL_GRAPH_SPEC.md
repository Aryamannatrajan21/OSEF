# Call Graph Specification

Call Graph edges are represented as `CALLS` relations in the Engineering Knowledge Graph.

## 1. Parsing Phase
The Parser identifies `ast.Call` nodes and assigns them to the invoking symbol's metadata string: `"calls": "my_function"`.

## 2. Semantic Phase
The `RelationshipEnricher` resolves these strings into actual canonical `Symbol` IDs and attaches them to `Symbol.related_ids["CALLS"]`.

## 3. EKG Phase
The `EKGBuilder` consumes the `related_ids` and injects deterministic `Edge` structures into the graph.

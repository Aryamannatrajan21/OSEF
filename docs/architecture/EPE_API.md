# EPE API Reference

The EPE API revolves around the `RuleContext` and its semantic query capabilities.

## `RuleContext`
- `get_nodes_by_type(node_type: str) -> List[Node]`
- `get_nodes_by_semantic_role(role: str) -> List[Node]`
- `get_edges_by_type(relation_type: str) -> List[Edge]`
- `find_dependencies() -> List[Edge]`
- `find_calls() -> List[Edge]`

All queries are memoized internally to guarantee optimal execution times across hundreds of rules.

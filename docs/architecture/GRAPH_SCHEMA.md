# Engineering Knowledge Graph Schema

The Engineering Knowledge Graph (EKG) is the final consumable artifact of the parser and resolution subsystem. It maps perfectly from the Symbol Table.

## 1. Nodes
Nodes represent Symbols.
- **id**: Maps 1:1 to `Symbol.id`
- **type**: Maps 1:1 to `Symbol.type`
- **name**: Maps 1:1 to `Symbol.name`
- **description**: Maps 1:1 to `Symbol.docstring`
- **metadata**: A flattened map of all properties (file path, visibility, is_async).

## 2. Edges
Edges represent semantic relationships between Nodes.

Supported Relation Types:
- `CONTAINS`: A module contains a class; a class contains a method. (Derived from `children_ids`)
- `IMPORTS`: An import symbol resolves to a concrete module or class.
- `INHERITS`: A class extends another class.
- `CALLS`: A method invokes another method.
- `RETURNS`: A method produces a specific Type Node.

## 3. Invariants
- Graph must be fully connected (except for totally isolated entry points).
- No dangling edges: `edge.source_id` and `edge.target_id` must exist in `graph.nodes`.
- IDs must remain stable between unchanged parses.

# GraphQuery Specification

`GraphQuery` is the **Traversal** layer of OSEF.

## Responsibility
It provides generic, semantic-free graph algorithms for navigating the Engineering Knowledge Graph.

**It does NOT:**
- Understand engineering concepts (e.g. "blast radius" or "deployment").
- Modify the graph.

## Categories of Traversal

### 1. Retrieval
- `get_node(node_id)`
- `get_edge(edge_id)`

### 2. Traversal
- `neighbors(node_id)`
- `successors(node_id)`
- `predecessors(node_id)`

### 3. Paths
- `find_path(source_id, target_id)`
- `trace(start_id, edge_type)`

### 4. Reachability
- `reachable(node_id)`
- `ancestors(node_id)`
- `descendants(node_id)`

### 5. Views
- `subgraph(node_ids)`
- `layer(node_type)`

### 6. Analysis
- `connected_components()`

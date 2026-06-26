# Semantic Model

The Semantic Model defines how generic concepts map to the Engineering Knowledge Graph.

## 1. Visibility Rules
- **public**: Default for all exported classes/functions.
- **protected**: Prefixed with a single underscore (e.g., `_helper`).
- **private**: Prefixed with double underscores (e.g., `__internal`).

## 2. Resolution Mechanics
- **Unresolved Imports**: Marked with `metadata["resolved"] = "false"`. The graph retains the import intent but points to no target.
- **Type Hints**: Resolved to their canonical base node. If a type hint is standard (e.g., `str`), it connects to a virtual "stdlib" node.

## 3. Engineering Assessments
Later stages of the pipeline will attach rich domain objects to the Graph metadata:
```json
{
  "assessment": {
    "architecture_violations": 0,
    "documentation_coverage": 0.85
  }
}
```

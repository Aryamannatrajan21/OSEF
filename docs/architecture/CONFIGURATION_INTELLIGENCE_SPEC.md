# Configuration Intelligence Specification

Configuration is treated as first-class engineering metadata in OSEF.

## 1. Supported Formats
The `ConfigParser` currently tracks `pyproject.toml` and `requirements.txt`.

## 2. Representation
Configuration files must be mapped directly into the `SymbolTable` as `Symbol(type="configuration")`.

## 3. Downstream Propagation
Analyzers read the `configuration` nodes in the EKG to assess build constraints, packaging tools, and external dependencies.

# Parser Contract

This contract dictates how new languages (e.g., JavaScript, Go, Rust, Java) are integrated into OSEF.

## 1. Responsibilities
A language parser is ONLY responsible for traversing the raw source code and populating a valid `SymbolTable`.

## 2. Prohibitions
- A parser **MUST NOT** directly instantiate `Node` or `Edge` objects.
- A parser **MUST NOT** perform deep dependency resolution (that is the job of Resolvers).
- A parser **MUST NOT** infer semantic intent like "Controller" or "Service" (that is the job of the Intelligence Layer).

## 3. API Requirements
Every parser must implement:
```python
class ParserContract:
    def __init__(self, symbol_table: SymbolTable):
        ...
        
    def parse_file(self, file_path: str) -> None:
        ...
```

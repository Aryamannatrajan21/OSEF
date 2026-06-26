# Analyzer Interface

All Analyzers within OSEF must implement `BaseAnalyzer` located in `osef.analyzers.base`.

## 1. Input Constraints
Analyzers may **only** consume the `KnowledgeGraph` (`osef.core.ekg.KnowledgeGraph`). They must never read the `SymbolTable` or access the file system.

## 2. Output Constraints
Analyzers must return factual findings. They do not calculate subjective metrics. Subjectivity is the responsibility of the Intelligence Layer.

## 3. Example
```python
class ArchitectureAnalyzer(BaseAnalyzer):
    def analyze(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        # Returns factual component counts based on semantic labels.
        pass
```

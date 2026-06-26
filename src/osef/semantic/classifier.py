"""
Semantic Classifier for heuristic-based intent detection.
"""

from osef.parser.symbol_table import SymbolTable, Symbol


class SemanticClassifier:
    """
    Infers engineering intent from raw symbols.
    """
    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table

    def classify_all(self) -> None:
        """
        Classifies all symbols in the table.
        """
        for symbol in self.symbol_table.symbols.values():
            if symbol.type == "class":
                self._classify_class(symbol)
            elif symbol.type in ("function", "method"):
                self._classify_function(symbol)

    def _classify_class(self, symbol: Symbol) -> None:
        name = symbol.name.lower()
        bases = symbol.metadata.get("bases", "").lower()
        
        classification = "Component"
        
        if "service" in name:
            classification = "Service"
        elif "controller" in name or "router" in name:
            classification = "Controller"
        elif "repository" in name or "dao" in name:
            classification = "Repository"
        elif "dto" in name or "basemodel" in bases:
            classification = "DTO"
        elif "exception" in bases or "error" in bases:
            classification = "Exception"
            
        symbol.metadata["semantic_role"] = classification

    def _classify_function(self, symbol: Symbol) -> None:
        name = symbol.name.lower()
        decs = symbol.metadata.get("decorators", "").lower()
        
        classification = "Function"
        
        if "get" in decs or "post" in decs or "put" in decs or "delete" in decs or "router" in decs:
            classification = "API_Endpoint"
        elif "command" in decs:
            classification = "CLI_Command"
        elif name.startswith("test_"):
            classification = "Test"
            
        symbol.metadata["semantic_role"] = classification

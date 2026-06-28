from typing import List, Sequence
from osef.sdk.language.symbols import NormalizedSymbol
from osef.sdk.language.builder import NormalizedSymbolBuilder
from src.parser.adapter import NormalizedASTNode

class TypeScriptSymbolExtractor:
    """
    Translates a parser-specific NormalizedAST into the parser-independent NormalizedSymbolModel.
    Extraction is strictly limited to identifying symbols; it does NOT resolve relationships.
    Executes in deterministic passes:
    1. Namespaces / Modules
    2. Types (Class, Interface, Enum, TypeAlias)
    3. Functions / Methods
    4. Variables / Constants
    5. Imports / Exports (Declarations only)
    6. Metadata (Decorators, Modifiers, Generics)
    """
    def __init__(self, builder: NormalizedSymbolBuilder):
        self.builder = builder

    def extract(self, ast: NormalizedASTNode) -> Sequence[NormalizedSymbol]:
        symbols: List[NormalizedSymbol] = []
        
        # In a full implementation, this extracts symbols via deterministic passes.
        # Pass 1: Namespaces / Modules
        # Pass 2: Types
        # Pass 3: Functions / Methods
        # Pass 4: Variables / Constants
        # Pass 5: Imports / Exports
        # Pass 6: Metadata
        
        return symbols

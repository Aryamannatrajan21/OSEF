"""
Symbol Table (Intermediate Representation).

This is the canonical semantic foundation of OSEF. All language parsers
must eventually populate this structure.
"""

import hashlib
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field


class SourceLocation(BaseModel):
    """Precise source code location."""

    line: int
    column: int
    end_line: Optional[int] = None
    end_column: Optional[int] = None


class Symbol(BaseModel):
    """
    A semantic component in the software architecture.
    """

    id: str
    name: str
    type: str  # package, module, class, method, function, variable, import
    file_path: str
    location: Optional[SourceLocation] = None
    docstring: Optional[str] = None
    visibility: str = "public"  # public, protected, private
    metadata: Dict[str, Any] = Field(default_factory=dict)

    # Relationships
    parent_id: Optional[str] = None
    children_ids: List[str] = Field(default_factory=list)
    related_ids: Dict[str, List[str]] = Field(default_factory=dict)


class SymbolTable:
    """
    The global registry for all extracted software components.
    """

    def __init__(self) -> None:
        self.symbols: Dict[str, Symbol] = {}
        self._type_index: Dict[str, List[Symbol]] = {}

    def generate_id(self, *parts: str) -> str:
        """Generate a deterministic ID based on parts."""
        return hashlib.sha256(":".join(parts).encode("utf-8")).hexdigest()[:16]

    def add_symbol(self, symbol: Symbol) -> None:
        """Register a symbol in the table."""
        self.symbols[symbol.id] = symbol
        
        if symbol.type not in self._type_index:
            self._type_index[symbol.type] = []
        self._type_index[symbol.type].append(symbol)

        if symbol.parent_id and symbol.parent_id in self.symbols:
            parent = self.symbols[symbol.parent_id]
            if symbol.id not in parent.children_ids:
                parent.children_ids.append(symbol.id)

    def get_symbol(self, symbol_id: str) -> Optional[Symbol]:
        """Retrieve a symbol by its ID."""
        return self.symbols.get(symbol_id)

    def find_by_type(self, symbol_type: str) -> List[Symbol]:
        """Find all symbols of a specific type."""
        return self._type_index.get(symbol_type, [])

    def get_children(self, symbol_id: str) -> List[Symbol]:
        """Get all children of a specific symbol."""
        symbol = self.get_symbol(symbol_id)
        if not symbol:
            return []
        children = []
        for child_id in symbol.children_ids:
            child = self.get_symbol(child_id)
            if child:
                children.append(child)
        return children

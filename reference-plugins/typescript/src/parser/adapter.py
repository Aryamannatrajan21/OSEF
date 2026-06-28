from typing import Protocol, List, Optional
from pydantic import BaseModel, Field

class NormalizedASTNode(BaseModel):
    """A normalized representation of an AST node to keep the semantic engine parser-agnostic."""
    kind: str
    text: str
    start_line: int
    start_column: int
    end_line: int
    end_column: int
    children: List['NormalizedASTNode'] = Field(default_factory=list)


class LanguageParserAdapter(Protocol):
    """
    Protocol defining the contract for any parser backend 
    (e.g., Tree-sitter, SWC, TypeScript Compiler API).
    """
    
    def parse(self, source_file: str) -> NormalizedASTNode:
        """Parse a source file and return a NormalizedASTNode."""
        ...

    def parser_name(self) -> str:
        """Return the name of the parser backend (e.g., 'tree-sitter')."""
        ...

    def parser_version(self) -> str:
        """Return the version of the parser backend."""
        ...

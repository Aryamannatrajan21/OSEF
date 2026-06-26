"""
Configuration Parser.
"""

from pathlib import Path
from osef.parser.symbol_table import SymbolTable, Symbol


class ConfigParser:
    """
    Parses repository configuration files into the SymbolTable.
    """
    def __init__(self, root_path: Path, symbol_table: SymbolTable):
        self.root_path = root_path
        self.symbol_table = symbol_table

    def parse_all(self) -> None:
        self._parse_pyproject()
        self._parse_requirements()
        
    def _parse_pyproject(self) -> None:
        path = self.root_path / "pyproject.toml"
        if not path.exists():
            return
            
        sym_id = self.symbol_table.generate_id("configuration", "pyproject.toml")
        sym = Symbol(
            id=sym_id,
            name="pyproject.toml",
            type="configuration",
            file_path=str(path),
            metadata={"format": "toml"}
        )
        self.symbol_table.add_symbol(sym)

    def _parse_requirements(self) -> None:
        path = self.root_path / "requirements.txt"
        if not path.exists():
            return
            
        sym_id = self.symbol_table.generate_id("configuration", "requirements.txt")
        sym = Symbol(
            id=sym_id,
            name="requirements.txt",
            type="configuration",
            file_path=str(path),
            metadata={"format": "txt"}
        )
        self.symbol_table.add_symbol(sym)

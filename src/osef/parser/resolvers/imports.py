"""
Import Resolution Engine.
"""

from osef.parser.symbol_table import SymbolTable


class ImportResolver:
    """
    Resolves import statements to concrete symbols within the SymbolTable.
    """
    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table

    def resolve(self) -> None:
        """
        Attempt to resolve all imports.
        """
        imports = self.symbol_table.find_by_type("import")
        
        for imp in imports:
            # Mark as unresolved by default
            imp.metadata["resolved"] = "false"
            
            # Simple heuristic matching for now
            target = imp.metadata.get("module") or imp.name
            
            # Search for matching module
            for mod in self.symbol_table.find_by_type("module"):
                # If the module's file path loosely matches the import target
                if target.replace(".", "/") in mod.file_path:
                    imp.metadata["resolved"] = "true"
                    imp.metadata["resolved_to"] = mod.id
                    break

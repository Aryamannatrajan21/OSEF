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
        modules = self.symbol_table.find_by_type("module")

        for imp in imports:
            # Mark as unresolved by default
            imp.metadata["resolved"] = "false"

            # Simple heuristic matching for now
            target = imp.metadata.get("module") or imp.name

            # Search for matching module
            target_path = target.replace(".", "/")
            for mod in modules:
                # If the module's file path loosely matches the import target
                if target_path in mod.file_path:
                    imp.metadata["resolved"] = "true"
                    imp.metadata["resolved_to"] = mod.id
                    break

            if imp.metadata.get("resolved") != "true":
                top_level = target.split(".")[0]
                try:
                    import sys
                    import importlib.util

                    if top_level in getattr(sys, "stdlib_module_names", ()):
                        imp.metadata["resolved"] = "true"
                        imp.metadata["resolved_to"] = f"stdlib:{top_level}"
                        imp.metadata["is_external"] = "true"
                    elif importlib.util.find_spec(top_level) is not None:
                        imp.metadata["resolved"] = "true"
                        imp.metadata["resolved_to"] = f"package:{top_level}"
                        imp.metadata["is_external"] = "true"
                except Exception:
                    pass

import re
from osef.parser.symbol_table import SymbolTable, Symbol, SourceLocation


class JavaParser:
    """
    Lightweight fallback parser for Java files using Regex.
    Extracts basic packages, classes, interfaces, enums, methods, and imports.
    """

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table

    def parse_file(self, file_path: str):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            return

        module_id = self.symbol_table.generate_id("module", file_path)
        module_symbol = Symbol(
            id=module_id,
            name=file_path.split("/")[-1],
            type="module",
            file_path=file_path,
        )
        self.symbol_table.add_symbol(module_symbol)

        lines = content.split("\n")

        # Regex patterns
        import_pattern = re.compile(r"import\s+(.*?);")
        class_pattern = re.compile(
            r"(?:public\s+|private\s+|protected\s+)?(?:abstract\s+|final\s+)?(class|interface|enum)\s+(\w+)"
        )
        func_pattern = re.compile(
            r"(?:public\s+|private\s+|protected\s+)?(?:static\s+|final\s+)?[\w\<\>\[\]]+\s+(\w+)\s*\("
        )

        for i, line in enumerate(lines):
            # parse imports
            import_match = import_pattern.search(line)
            if import_match:
                module = import_match.group(1)
                import_id = self.symbol_table.generate_id("import", file_path, module)
                import_sym = Symbol(
                    id=import_id,
                    name=module,
                    type="import",
                    file_path=file_path,
                    location=SourceLocation(line=i + 1, column=0),
                    parent_id=module_id,
                    metadata={"module": module},
                )
                self.symbol_table.add_symbol(import_sym)
                continue

            class_match = class_pattern.search(line)
            if class_match:
                type_ = class_match.group(1)
                name = class_match.group(2)
                cls_id = self.symbol_table.generate_id("class", file_path, name)
                cls_sym = Symbol(
                    id=cls_id,
                    name=name,
                    type="class"
                    if type_ == "class"
                    else ("interface" if type_ == "interface" else "enum"),
                    file_path=file_path,
                    location=SourceLocation(line=i + 1, column=0),
                    parent_id=module_id,
                )
                self.symbol_table.add_symbol(cls_sym)
                continue

            # Naive function parsing, ignore keywords like if, for, while, switch, catch
            func_match = func_pattern.search(line)
            if func_match:
                name = func_match.group(1)
                if name not in ("if", "for", "while", "switch", "catch"):
                    func_id = self.symbol_table.generate_id("function", file_path, name)
                    func_sym = Symbol(
                        id=func_id,
                        name=name,
                        type="function",
                        file_path=file_path,
                        location=SourceLocation(line=i + 1, column=0),
                        parent_id=module_id,
                    )
                    self.symbol_table.add_symbol(func_sym)

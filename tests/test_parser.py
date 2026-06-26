from osef.parser.python import PythonParser
from osef.parser.symbol_table import SymbolTable


def test_parser_populates_symbol_table():
    source = '''
"""Module docstring"""
import os
from typing import List

@decorator
class MyClass(Base):
    """Class docstring"""
    
    @classmethod
    def my_method(cls):
        pass
        
async def my_async_func():
    pass
'''
    table = SymbolTable()
    parser = PythonParser(table)
    parser.parse_source(source, "test_file.py")

    # Check Module
    modules = table.find_by_type("module")
    assert len(modules) == 1
    assert modules[0].docstring == "Module docstring"

    # Check Imports
    imports = table.find_by_type("import")
    assert len(imports) == 2
    assert imports[1].name == "List"
    assert imports[1].metadata["module"] == "typing"

    # Check Class
    classes = table.find_by_type("class")
    assert len(classes) == 1
    assert classes[0].name == "MyClass"
    assert classes[0].docstring == "Class docstring"
    assert classes[0].metadata["bases"] == "Base"
    assert classes[0].metadata["decorators"] == "decorator"

    # Check Method
    methods = table.find_by_type("method")
    assert len(methods) == 1
    assert methods[0].name == "my_method"

    # Check Function
    functions = table.find_by_type("function")
    assert len(functions) == 1
    assert functions[0].name == "my_async_func"
    assert functions[0].metadata["is_async"] == "true"

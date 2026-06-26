from osef.parser.python import PythonParser

def test_parser_extracts_ast():
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
    parser = PythonParser()
    module = parser.parse_source(source)
    
    assert module.docstring == "Module docstring"
    assert len(module.imports) == 2
    assert module.imports[1].module == "typing"
    assert module.imports[1].names == ["List"]
    
    assert len(module.classes) == 1
    cls = module.classes[0]
    assert cls.name == "MyClass"
    assert cls.bases == ["Base"]
    assert cls.docstring == "Class docstring"
    assert len(cls.decorators) == 1
    assert cls.decorators[0].name == "decorator"
    
    assert len(cls.methods) == 1
    assert cls.methods[0].name == "my_method"
    
    assert len(module.functions) == 1
    assert module.functions[0].name == "my_async_func"
    assert module.functions[0].is_async is True

# Symbol Table Specification (IR)

The Symbol Table is the definitive Intermediate Representation (IR) of the OSEF framework. All language-specific parsers must converge to this specification.

## 1. Abstract Symbol Schema

Every extracted entity is a `Symbol`. The `Symbol` interface is strictly defined:

```python
class SourceLocation(BaseModel):
    line: int
    column: int
    end_line: Optional[int]
    end_column: Optional[int]

class Symbol(BaseModel):
    id: str                 # Deterministic hash of its canonical path
    name: str               # Short identifier (e.g., 'MyClass', 'parse_file')
    type: str               # package, module, class, method, function, variable, import
    file_path: str          # Physical absolute path
    location: Optional[SourceLocation]
    docstring: Optional[str]
    visibility: str         # 'public', 'protected', 'private'
    metadata: Dict[str, Any]
    parent_id: Optional[str]
    children_ids: List[str]
```

## 2. Supported Symbol Types
- **package**: A directory containing modules.
- **module**: A file containing source code.
- **class**: An object-oriented class definition.
- **method**: A function bound to a class.
- **function**: A standalone function definition.
- **variable**: A global or class-level variable.
- **import**: A dependency resolution instruction.

## 3. ID Determinism
IDs must be generated deterministically to guarantee graph stability across multiple scanner runs.
Format: `hash(type : file_path : parent_id : name)`

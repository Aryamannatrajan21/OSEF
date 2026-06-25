# OSEF Coding Standards

## 1. Protocol-First Interfaces
Use `typing.Protocol` to define service contracts. Do not use `abc.ABC` unless providing shared framework logic (like `BasePlugin`).
```python
from typing import Protocol

class StorageProvider(Protocol):
    async def read(self, path: str) -> bytes: ...
```

## 2. Dependency Injection
Never instantiate a Service inside another Service. Inject it via the constructor.
```python
# Bad
class Engine:
    def __init__(self):
        self.bus = EventBus()

# Good
class Engine:
    def __init__(self, bus: EventBusProvider):
        self.bus = bus
```

## 3. Strict Typing
Use Python 3.13+ type annotations everywhere. `Any` is strongly discouraged.
```python
# Good
def publish(events: list[Event]) -> None: ...
```

## 4. Immutable Domain Models
Data passed through the Event Bus must be immutable to prevent side-effects from concurrent async tasks.
```python
from pydantic import BaseModel, ConfigDict

class Event(BaseModel):
    model_config = ConfigDict(frozen=True)
    payload: dict[str, str]
```

## 5. Event-Driven Communication
Services should not call each other directly unless strictly necessary. They should publish events.
```python
# Instead of calling Logger directly:
await self.bus.publish(ProjectAnalyzedEvent(score=95))
```

## 6. No Business Logic in the CLI
The `cli/` module handles `Typer` arguments, calls the Core SDK, and formats the response using `Rich`. It must not contain `if/else` chains determining Open Source compliance logic.

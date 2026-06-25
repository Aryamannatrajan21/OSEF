# OSEF Public API Specification

## Overview
The Public API is the stable interface exposed to developers and plugins. It is governed by Semantic Versioning; breaking changes here require a major version release.

## 1. Import Boundaries
The Public API is strictly confined to the following module paths:
- `osef.contracts.*`
- `osef.interfaces.*`
- `osef.core.context`

## 2. Core Protocols (`osef.contracts.providers`)
These protocols define the capabilities plugins can rely on or implement.
- `EventBusProvider`: `async def publish(event: Event)`, `def subscribe(event_type: str, handler: Callable)`
- `KnowledgeProvider`: `async def search(tags: list[str]) -> list[KnowledgeItem]`
- `StorageProvider`: `async def read(path: str) -> bytes`, `async def write(path: str, content: bytes)`
- `ValidationProvider`: `async def validate(context: Context) -> ValidationResult`

## 3. Domain Models (`osef.contracts.models`)
Immutable Pydantic models and dataclasses passed between services.
- `Event`: Base event model with `event_id`, `session_id`, `payload`.
- `ProjectContext`: Describes the repository being analyzed.
- `KnowledgeItem`: A distinct rule or document from the EKK.
- `CertificationScore`: The result of an OSTE evaluation.

## 4. Plugin Base Classes (`osef.interfaces.plugin`)
The abstract base classes required for community extensions.
```python
from abc import ABC, abstractmethod
from osef.contracts.providers import EventBusProvider

class BasePlugin(ABC):
    name: str
    version: str
    
    @abstractmethod
    async def register_hooks(self, event_bus: EventBusProvider) -> None:
        """Called during core bootstrapping."""
```

## 5. SDK Entry Point (`osef.__init__`)
The primary programmatic interface for initializing OSEF.
```python
import osef
from osef.contracts.models import ProjectConfig

async def init(config: ProjectConfig) -> 'CoreContainer':
    """Bootstraps the DI container and loads plugins."""
```

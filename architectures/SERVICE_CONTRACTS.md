# OSEF Service Contracts Architecture

## Overview
This document defines the abstract service interfaces (Protocols) for the core subsystems of OSEF. In accordance with the Interface-First Architecture principle, all inter-service communication and external extensions must program against these Protocols, not concrete implementations. All protocols must support future asynchronous execution.

---

## Core Protocols (`typing.Protocol`)

### 1. `KnowledgeProvider`
**Responsibility:** Interface for retrieving and querying the Engineering Knowledge Kernel (EKK).
```python
from typing import Protocol, List, Optional
from osef.contracts.models import KnowledgeItem

class KnowledgeProvider(Protocol):
    async def get_item(self, item_id: str) -> Optional[KnowledgeItem]:
        ...
    
    async def search(self, tags: List[str], context: str) -> List[KnowledgeItem]:
        ...
        
    async def get_dependencies(self, item_id: str) -> List[KnowledgeItem]:
        ...
```

### 2. `StorageProvider`
**Responsibility:** Abstract persistence layer for Knowledge, Artifacts, and Configuration.
```python
from typing import Protocol, Any, Dict

class StorageProvider(Protocol):
    async def read(self, path: str) -> bytes:
        ...
        
    async def write(self, path: str, content: bytes) -> None:
        ...
        
    async def list_items(self, prefix: str) -> List[str]:
        ...
```

### 3. `PluginProvider`
**Responsibility:** Interface for plugin discovery, registration, and lifecycle management.
```python
from typing import Protocol
from osef.contracts.models import PluginMetadata

class PluginProvider(Protocol):
    async def discover(self) -> List[PluginMetadata]:
        ...
        
    async def load(self, plugin_id: str) -> None:
        ...
        
    async def register_hooks(self) -> None:
        ...
```

### 4. `EventBusProvider`
**Responsibility:** Publish/Subscribe routing for all system events.
```python
from typing import Protocol, Callable, Any
from osef.contracts.events import Event

class EventBusProvider(Protocol):
    async def publish(self, event: Event) -> None:
        ...
        
    def subscribe(self, event_type: str, handler: Callable[[Event], Any]) -> None:
        ...
```

### 5. `ValidationProvider`
**Responsibility:** Interface for asserting compliance against Engineering Knowledge.
```python
from typing import Protocol
from osef.contracts.models import ValidationResult, Artifact

class ValidationProvider(Protocol):
    async def validate(self, artifact: Artifact, context: Any) -> ValidationResult:
        ...
```

### 6. `AgentProvider`
**Responsibility:** Interface for invoking and monitoring autonomous reasoning agents.
```python
from typing import Protocol
from osef.contracts.models import Workflow, TaskResult

class AgentProvider(Protocol):
    async def execute_workflow(self, workflow: Workflow) -> TaskResult:
        ...
        
    async def status(self, execution_id: str) -> str:
        ...
```

### 7. `ConfigurationProvider`
**Responsibility:** Read-only access to merged configuration state.
```python
from typing import Protocol, Any, Optional

class ConfigurationProvider(Protocol):
    def get(self, key: str, default: Optional[Any] = None) -> Any:
        ...
```

---

## Shared Framework ABCs (`abc.ABC`)

As dictated by the architectural rules, `abc.ABC` is reserved *strictly* for shared framework behavior, not defining interfaces.

### 1. `BasePlugin(abc.ABC)`
Provides default hook registration wrappers and logging setup for community plugins.

### 2. `BaseAgent(abc.ABC)`
Provides shared metric emission, telemetry, and default error handling (Exception Groups) for Agent implementations.

### 3. `BaseStorageAdapter(abc.ABC)`
Provides common caching and path resolution utilities for storage backends like Markdown, SQLite, or Network storage.

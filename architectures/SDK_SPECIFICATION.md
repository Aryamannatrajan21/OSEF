# OSEF SDK Specification

## Overview
The OSEF Public Python SDK is the official programmatic interface for integrating with the framework. It exposes the stable Service Contracts (Protocols) defined in `SERVICE_CONTRACTS.md`, ensuring that third-party developers, IDE integrations, and custom plugins interact with OSEF through consistent, implementation-agnostic boundaries.

## 1. Design Principles
- **Protocol-Oriented:** The SDK primarily exposes `typing.Protocol` interfaces and immutable `dataclass` models.
- **Async-First:** Top-level functions and interface methods are `async def` to support future network boundaries.
- **Fluent API:** Core configuration and initialization use builder patterns or declarative Pydantic models.
- **Dependency Injection:** The SDK automatically resolves dependencies (e.g., wiring the Event Bus to the Knowledge Provider) when initializing the Core.

---

## 2. Package Structure
```
osef/
  __init__.py          # Facade: Top-level entry point (osef.init)
  contracts/           # Protocols, Domain Models, Events
  interfaces/          # Framework-specific ABCs (e.g., BasePlugin)
  core/                # The Dependency Injection container and Bootstrapper
  services/            # (Internal) Concrete implementations
  adapters/            # (Internal) Storage adapters
  plugins/             # Built-in plugins
```

---

## 3. Core Initialization
The SDK provides a simple bootstrap mechanism to instantiate a Session with requested Providers.

```python
import asyncio
import osef
from osef.contracts.models import ProjectConfig

async def main():
    # Initialize the core container
    core = await osef.init(
        config=ProjectConfig(path="./my_project"),
        storage_adapter="markdown",  # Resolves internal implementation
        plugins=["osef_security", "custom_reviewer"]
    )
    
    # Retrieve protocol instances via the container
    knowledge_provider = core.get_knowledge_provider()
    agent_provider = core.get_agent_provider()
```

---

## 4. Working with the Engineering Knowledge Kernel (EKK)
```python
async def query_knowledge(core: osef.Core):
    provider = core.get_knowledge_provider()
    
    # Semantic/Tag lookup
    items = await provider.search(tags=["architecture", "python"], context="API Design")
    for item in items:
        print(f"[{item.item_id}] {item.summary}")
```

---

## 5. Plugin Authoring
Third-party developers import `contracts` and `interfaces` to build plugins.

```python
from osef.interfaces import BasePlugin
from osef.contracts import PluginProvider, EventBusProvider
from osef.contracts.events import ProjectAnalyzed

class MyCustomPlugin(BasePlugin):
    name = "my_custom_plugin"
    version = "1.0.0"
    
    async def register_hooks(self, event_bus: EventBusProvider) -> None:
        event_bus.subscribe("ProjectAnalyzed", self.on_project_analyzed)
        
    async def on_project_analyzed(self, event: ProjectAnalyzed) -> None:
        self.logger.info(f"Analyzing {event.payload['repo_path']}")
```

---

## 6. Stability Guarantees
- Everything importable from `osef.contracts.*` and `osef.interfaces.*` is covered by strict Semantic Versioning.
- Breaking changes require a major version bump, an RFC, and an ADR.
- Code within `osef.services.*` is strictly internal; importing from here is unsupported and unversioned.

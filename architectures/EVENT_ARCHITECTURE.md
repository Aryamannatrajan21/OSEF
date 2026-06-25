# OSEF Event Architecture

## Overview
OSEF is an event-driven framework. Subsystems communicate through the Event Bus to minimize coupling. Services publish events when their state changes or when an action is completed, allowing other services (or plugins) to react asynchronously.

---

## 1. Event Bus Architecture

### Responsibilities
- Route events from publishers to subscribers.
- Enforce event metadata constraints.
- Prioritize event delivery (e.g., synchronous UI updates vs asynchronous logging).
- Provide hooks for future Event Persistence and Event Replay functionality.

### Core Components
- **Publisher:** Any Service or Plugin implementing a Service Contract.
- **EventBusProvider:** The central routing mechanism.
- **Subscriber:** Callbacks or async tasks registered to specific Event Types.

---

## 2. Event Metadata Structure

All events in OSEF inherit from a base immutable `dataclass` model.

```python
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any
import uuid

@dataclass(frozen=True)
class Event:
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str = field(init=False)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    session_id: str
    source: str
    payload: Dict[str, Any]
    priority: int = 1  # 0=Critical, 1=High, 2=Normal, 3=Low
```

---

## 3. Canonical Event Types

### Lifecycle Events
- `SystemInitialized`: Core services are loaded.
- `SessionStarted`: A user session or workflow begins.
- `SessionEnded`: The session completes and memory is finalized.

### Plugin Events
- `PluginRegistered`: A new plugin is discovered.
- `PluginLoaded`: A plugin's hooks are active.

### Knowledge Events
- `KnowledgeLoaded`: The EKK has finished parsing storage.
- `KnowledgeUpdated`: A node in the EKK has mutated.
- `KnowledgeValidated`: EKK integrity checks passed.

### Project & Repository Events
- `RepositoryAnalyzed`: Source tree parsing completed.
- `ProjectMutated`: A file was created, modified, or deleted by OSEF.

### Agent & Workflow Events
- `WorkflowStarted`: An orchestration sequence begins.
- `TaskCompleted`: An individual workflow step finishes.
- `AgentReasoning`: Agent emits internal chain-of-thought (Low priority, for tracing).
- `ValidationFailed`: An architectural or security check failed (Critical priority).

---

## 4. Event Routing & Lifecycle

### Synchronous vs Asynchronous Delivery
By default, the `EventBusProvider` supports asynchronous delivery using Python's `asyncio`.
- **Critical Priority (0):** Processed immediately, can optionally block the publisher if strict sequential validation is required.
- **Normal/Low Priority (2-3):** Fire-and-forget. Queued and processed in the background (e.g., Telemetry, Logging).

### Event Flow Example
1. `KnowledgeService` loads `ADR-0002.md`.
2. `KnowledgeService` publishes `KnowledgeUpdated` event.
3. `EventBusProvider` receives the event.
4. `ValidationService` (subscriber) receives the event and re-validates related artifacts.
5. `PromptEngine` (subscriber) receives the event and invalidates prompt caches.

---

## 5. Future Extensibility
The Event Architecture is designed to easily accommodate:
- **Event Persistence:** Saving all events to SQLite for audit trails.
- **Event Replay:** Reconstructing a Session's state by replaying past events.
- **Distributed Events:** Bridging the local Event Bus to a Redis or Kafka queue for multi-agent cloud deployments.

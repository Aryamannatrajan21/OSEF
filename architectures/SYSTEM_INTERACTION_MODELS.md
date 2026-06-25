# OSEF System Interaction Models

## Overview
This document visualizes the runtime interactions of OSEF using Mermaid.js diagrams. It maps how the components defined in the Service Contracts and Domain Models interact to fulfill Workflows and Events.

---

## 1. Context Diagram
*How OSEF fits into the broader ecosystem.*

```mermaid
graph TD
    User([Developer / User]) --> CLI[OSEF CLI]
    User --> IDE[IDE Integration]
    IDE --> SDK[OSEF Public SDK]
    CLI --> SDK
    
    SDK --> Core[OSEF Core Runtime]
    Core --> EKK[(Engineering Knowledge Kernel)]
    Core --> Repo[(User Repository)]
    Core --> AI[AI Provider API]
    Core -.-> Plugins[Community Plugins]
```

---

## 2. Component Diagram
*The internal architecture of the OSEF Core.*

```mermaid
graph TD
    subgraph OSEF Core
        DI[Dependency Injector] --> EB[Event Bus Provider]
        DI --> KP[Knowledge Provider]
        DI --> AP[Agent Provider]
        DI --> VP[Validation Provider]
        DI --> PP[Plugin Provider]
        DI --> SP[Storage Provider]
    end
    
    EB <--> |Pub/Sub| KP
    EB <--> |Pub/Sub| AP
    EB <--> |Pub/Sub| VP
    EB <--> |Pub/Sub| PP
```

---

## 3. Event Flow
*Demonstrating the decoupled, event-driven architecture.*

```mermaid
sequenceDiagram
    participant RepoService
    participant EventBus
    participant KnowledgeService
    participant AgentRuntime
    
    RepoService->>EventBus: publish(ProjectAnalyzed)
    EventBus-->>KnowledgeService: ProjectAnalyzed
    KnowledgeService->>KnowledgeService: Fetch applicable rules for Python
    KnowledgeService->>EventBus: publish(KnowledgeLoaded)
    EventBus-->>AgentRuntime: KnowledgeLoaded
    AgentRuntime->>AgentRuntime: Begin workflow execution
```

---

## 4. Knowledge Retrieval Flow
*How the EKK serves the Agent Runtime.*

```mermaid
sequenceDiagram
    participant Agent
    participant PromptProvider
    participant KnowledgeProvider
    
    Agent->>PromptProvider: Request Context(task="Write Tests")
    PromptProvider->>KnowledgeProvider: search(tags=["testing"])
    KnowledgeProvider-->>PromptProvider: [KnowledgeItem(Testing Standard)]
    PromptProvider->>PromptProvider: Render Jinja Template
    PromptProvider-->>Agent: Rendered Prompt
    Agent->>AI: Send to LLM
```

---

## 5. Plugin Registration Flow
*How extensions integrate securely.*

```mermaid
sequenceDiagram
    participant Bootstrapper
    participant PluginProvider
    participant CustomPlugin
    participant EventBus
    
    Bootstrapper->>PluginProvider: discover()
    PluginProvider->>CustomPlugin: instantiate
    Bootstrapper->>PluginProvider: register_hooks(EventBus)
    PluginProvider->>CustomPlugin: register_hooks(EventBus)
    CustomPlugin->>EventBus: subscribe('ValidationStarted')
    CustomPlugin-->>EventBus: registered
```

---

## 6. Repository Analysis Flow
*How OSEF discovers the state of a user's code.*

```mermaid
sequenceDiagram
    participant Workflow
    participant RepoProvider
    participant StorageProvider
    participant EventBus
    
    Workflow->>RepoProvider: analyze(path)
    RepoProvider->>StorageProvider: list_files(path)
    StorageProvider-->>RepoProvider: tree
    RepoProvider->>EventBus: publish(RepositoryAnalyzed)
    EventBus-->>Workflow: acknowledge
```

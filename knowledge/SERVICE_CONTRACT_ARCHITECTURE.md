# OSEF Service Contract Architecture

## Protocol vs ABC Standards

### Architectural Principle
OSEF follows an Interface-First Architecture.
Service Contracts define capabilities.
Implementations provide behavior.
The system should maximize extensibility while minimizing coupling.
OSEF therefore distinguishes between Contracts and Framework Components.

### Rule 1 — Prefer Protocols
Default to `typing.Protocol`.
Protocols represent capabilities.
They should contain no implementation.
They should define only the public contract.

**Example:**
* KnowledgeProvider
* PluginProvider
* StorageProvider
* PromptProvider
* TemplateProvider
* RepositoryProvider
* DocumentationProvider
* ValidationProvider
* AgentProvider
* ConfigurationProvider

Protocols allow structural typing and make third-party plugins significantly easier to write.
This is the preferred pattern.

### Rule 2 — ABCs Only for Shared Framework Logic
Use `abc.ABC` only when multiple implementations genuinely require shared lifecycle behavior.

**Examples:**
* Plugin
* BaseAgent
* BaseValidator
* BaseGenerator
* BaseReviewer
* BaseStorageAdapter

These are framework base classes.
They may provide:
* default logging
* common validation
* registration helpers
* lifecycle hooks
* configuration loading
* metrics
* shared utility methods

ABCs should never exist simply to define an interface.

### Rule 3 — Domain Models
Use `dataclasses` or Pydantic models.
Never use inheritance-heavy object hierarchies.
Prefer immutable models whenever practical.

**Examples:**
* KnowledgeItem
* Project
* PluginMetadata
* Command
* Artifact
* RFC
* ADR
* Template
* Configuration
* Event

### Rule 4 — Composition
Prefer composition over inheritance.
A Service should consume:
* KnowledgeProvider
* StorageProvider
* Logger
* Configuration
* Validator

rather than inheriting from multiple base classes.

### Rule 5 — Dependency Injection
Every service depends on contracts.
Never on concrete implementations.

**Correct:**
ArchitectureService → KnowledgeProvider

**Incorrect:**
ArchitectureService → MarkdownKnowledgeProvider

Core should never know concrete implementations.

### Rule 6 — Plugin Contracts
Plugins should satisfy Protocols.
Plugins should not inherit from framework base classes unless lifecycle behavior is required.
This makes community plugins easier to implement.

### Rule 7 — Async Compatibility
Every Protocol should be designed to support asynchronous implementations in the future.
Avoid assumptions that services are synchronous.

Where practical:
* provide async interfaces
* allow synchronous wrappers

This enables future support for:
* remote APIs
* cloud knowledge
* vector databases
* graph databases
* distributed agents

### Rule 8 — Event Driven
Service Contracts should publish events.
They should not directly invoke unrelated services.

**Instead:**
KnowledgeLoaded → Event Bus → Documentation Service → Prompt Engine → Agent Runtime

This minimizes coupling.

### Rule 9 — Public SDK
The SDK exposes Protocols.
It does not expose implementations.
Third-party developers should program against interfaces, not internal classes.

### Rule 10 — Internal Architecture
Preferred structure:

* `contracts/`: Contains Protocols, Type Aliases, Enums, Exceptions, Value Objects
* `interfaces/`: Contains Framework-level contracts
* `services/`: Contains Implementations
* `adapters/`: Contains Markdown, YAML, JSON, SQLite, PostgreSQL, Graph, Vector
* `plugins/`: Contains Community implementations

This separation is mandatory.

### Rule 11 — Future Compatibility
Every contract should assume future support for:
* remote execution
* multiple processes
* network transport
* distributed agents
* plugin marketplaces
* cloud-hosted kernels

Do not design contracts that assume everything is local.

### Rule 12 — Python Philosophy
Use modern Python (3.13+).
* Protocol over inheritance.
* Dataclasses for lightweight immutable models.
* Pydantic only where validation is required.
* Enums instead of string constants.
* `pathlib` instead of `os.path`.
* Exception Groups where appropriate.
* Structural Pattern Matching where it improves readability.
* Strict mypy typing.
* ruff enforcement.
* No dynamic monkey patching.
* No hidden magic.
* No runtime metaclass tricks.
* Favor explicit, readable code.

### Final Architectural Decision
Default to **Protocols** for contracts.
Use **ABCs** only when shared framework behavior provides genuine value.
Everything else should rely on dependency injection, composition, and structural typing.
This architecture best supports OSEF's long-term goals of extensibility, maintainability, plugin interoperability, and AI-assisted evolution.

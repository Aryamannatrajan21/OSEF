# OSEF Implementation Order

## Canonical Sequence
No subsystem may begin implementation until its prerequisites are complete.

1. **Contracts (`contracts/`)**
   - *Why:* Defining the abstract `typing.Protocol` boundaries ensures that the Core and Plugins have a stable, decoupled vocabulary before any logic is written.
2. **Models (`contracts/models.py`)**
   - *Why:* The Event Bus and Services cannot be tested without the Pydantic models they pass around.
3. **Core Dependency Injection (`core/container.py`)**
   - *Why:* All services rely on DI to locate each other. Building this first ensures we never fall back on global singletons or circular imports.
4. **Internal Services (`services/`)**
   - *Why:* Implement the Event Bus and EKK router. These form the operating system's kernel.
5. **IO Adapters (`adapters/`)**
   - *Why:* Hooking SQLite and the FileSystem up to the Services allows them to actually persist data.
6. **Plugin Runtime (`core/plugins.py`)**
   - *Why:* Once Services exist, the Plugin runtime can be built to extend them.
7. **SDK Facade (`__init__.py`)**
   - *Why:* Wraps the DI container into a developer-friendly Python API.
8. **Transformation Engine (OSTE)**
   - *Why:* Requires the SDK, Event Bus, and EKK to be fully operational before it can analyze a repository.
9. **CLI Presentation (`cli/`)**
   - *Why:* The CLI contains zero business logic. It simply invokes the Transformation Engine and formats the output. It is built last.

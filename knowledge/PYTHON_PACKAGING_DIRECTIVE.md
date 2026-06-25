# OSEF Python Packaging Directive

## Minimal Core, Extensible Edge Philosophy

### Architectural Principle
Every dependency increases:
- Installation size
- Startup time
- Security surface
- Maintenance burden
- Compatibility risk
- Contributor friction

Therefore, dependencies must be treated as architectural decisions rather than implementation conveniences.

### Core Dependency Policy
The Core should depend only on:
- Python Standard Library
- Typer
- Pydantic
- Pydantic Settings
- Jinja2

*Additional dependencies require explicit architectural justification.*

### Storage
For the MVP, prefer the Python standard library (`sqlite3`) over ORM frameworks.
The storage layer must be defined through Service Contracts and adapters.
Future implementations (SQLAlchemy, PostgreSQL, graph databases, vector databases, cloud storage) shall be implemented as optional packages without requiring changes to the Core.

### Dependency Inversion
Every external system shall be accessed through an abstract service contract. Examples include:
- AI providers
- Storage backends
- Search engines
- Template engines
- Documentation generators
- Version control integrations

The Core depends on interfaces. Adapters depend on external libraries.

### Optional Features
Advanced capabilities should be distributed as independently installable packages. Examples:
- `osef-openai`, `osef-anthropic`, `osef-ollama`
- `osef-storage-postgres`, `osef-storage-sqlalchemy`
- `osef-storage-neo4j`, `osef-storage-qdrant`
- `osef-fastapi`, `osef-django`, `osef-react`, `osef-kubernetes`

Users install only the capabilities they require.

### Dependency Budget
The Core should maintain a minimal external dependency budget. Before introducing any new dependency, evaluate:
1. Can the standard library satisfy the requirement?
2. Can the functionality be implemented as an adapter?
3. Can it be implemented as a plugin?
4. Does the dependency create vendor lock-in?
5. Does it materially improve the architecture?

If the answer to these questions does not justify inclusion, the dependency should not be added to the Core.

### Long-Term Goal
The OSEF Core should remain lightweight, portable, secure, and easy to install. Complexity belongs at the edges of the architecture, not at its center. The architecture should enable powerful ecosystems without requiring every user to install every capability.

This principle is mandatory for all future packaging and dependency decisions.

# OSEF Graph Relationship Vocabulary Specification

To maintain consistency across the Engineering Knowledge Graph (EKG), all Knowledge Domains and the Cross-Domain Correlation Engine must utilize this canonical vocabulary for edge relationships.

## Structural Relationships (Intra-Domain)
Relationships that define the internal hierarchy or dependencies of a specific domain.

- `CONTAINS`: A parent node contains a child node (e.g., `Software.Package` -> `CONTAINS` -> `Software.Class`).
- `CALLS`: A function or method invokes another.
- `IMPORTS`: A module explicitly references another module.
- `IMPLEMENTS`: A class or struct fulfills an interface.

## Cross-Domain Relationships (Inter-Domain)
Relationships established by the Correlation Engine that bridge isolated Knowledge Domains.

- `DEPLOYED_AS`: Maps structural code to its operational artifact (e.g., `Software.Service` -> `DEPLOYED_AS` -> `Infrastructure.Container`).
- `RUNS_ON`: Maps a container or process to its host infrastructure (e.g., `Infrastructure.Container` -> `RUNS_ON` -> `Infrastructure.Node`).
- `DESCRIBES`: Maps documentation to the code or infrastructure it explains (e.g., `Documentation.API` -> `DESCRIBES` -> `Software.Service`).
- `AFFECTS`: Maps a security finding, vulnerability, or debt to the impacted node (e.g., `Security.Vulnerability` -> `AFFECTS` -> `Infrastructure.Container`).
- `OWNS`: Maps organizational entities to technical assets (e.g., `Enterprise.Team` -> `OWNS` -> `Software.Service`).
- `USES`: Generic usage of a resource or service.
- `DEPENDS_ON`: Runtime or architectural dependency between services or components.
- `PROTECTED_BY`: Maps an asset to a security control (e.g., `Infrastructure.Network` -> `PROTECTED_BY` -> `Security.Boundary`).
- `EXPOSES`: Maps internal assets to external ingress or APIs.
- `GENERATES`: Maps a process or system to the artifacts it creates.
- `REFERENCES`: Generic cross-link or mention (e.g., documentation linking to a policy).

*Note: New vocabulary must be proposed and approved via an Architecture Decision Record (ADR).*

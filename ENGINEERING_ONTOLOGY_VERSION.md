# OSEF Engineering Ontology Versioning

**Current Version:** 1.0.0

Tracking the stability of the Engineering Ontology is critical for external plugins, AI Agents, and the Enterprise Ecosystem.

| Component | Version | Description |
|-----------|---------|-------------|
| **Ontology Version** | `1.0.0` | The master version of this suite of specifications. |
| **Knowledge Model Version** | `1.0.0` | Defines the stability of the SKM, IKM, AKM, etc. |
| **Relationship Vocabulary Version** | `1.0.0` | The canonical edges (`DEPLOYED_AS`, `RUNS_ON`, etc.) |
| **Graph Schema Version** | `4.0.0` | The structural schema of `Node` and `Edge` objects in the EKG. |
| **Query API Version** | `1.0.0` | The interface contract for `GraphQuery` and `EngineeringReasoner`. |

Any breaking change to a component increments its version and the master Ontology Version.

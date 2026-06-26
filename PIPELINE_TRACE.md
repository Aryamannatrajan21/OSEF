# Pipeline Trace

Captures the execution trace and provider invocation timings of the Pipeline Engine.

| Stage | Provider / Implementer | Elapsed | Lifecycle Event |
| :--- | :--- | :--- | :--- |
| **Scanning** | `RepositoryScanner` (Core) | 0.02s | `BeforeRepositoryScan`, `AfterRepositoryScan` |
| **Parsing** | `PythonParserProvider` (`osef-python`) | 0.15s | `BeforeParsing`, `AfterParsing` |
| **Semantic** | Legacy Resolvers (Core) | 0.08s | `BeforeSemanticEnrichment`, `AfterSemanticEnrichment` |
| **Graph** | Node & Edge Construction (Core) | 0.05s | `BeforeGraphGeneration`, `AfterGraphGeneration` |
| **Policy** | `EngineeringPolicyEngine` (Core) | 0.12s | `BeforePolicyExecution`, `AfterPolicyExecution` |

*(This log is for reference and should be dynamically populated by a telemetry observer in future phases).*

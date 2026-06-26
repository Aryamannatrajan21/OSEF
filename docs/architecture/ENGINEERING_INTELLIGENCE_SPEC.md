# Engineering Intelligence Specification

The Intelligence Layer sits at the very top of OSEF's architectural stack. It does not parse code, it does not assign semantic tags, and it does not calculate graph edges. It acts strictly as an orchestrator.

## 1. Domain Object Returns
Primitive scores are prohibited. The Intelligence Layer must wrap all output in structured domain models (e.g., `EngineeringAssessment`, `ArchitectureAssessment`).

## 2. Rule Validation
Recommendations must be derived purely from the findings of individual Analyzers.

## 3. Contract
The Intelligence Layer is the **only** subsystem permitted to render analytical text or "opinions" about the repository.

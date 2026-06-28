# Java Language Mapping Specification

This document explicitly defines how Java constructs are mapped to the canonical OSEF Engineering Ontology without requiring any modifications to the core Language SDK v1.

## Structural Mappings
| Java Construct | Canonical SDK Abstraction | Confidence |
| -------------- | ------------------------- | ---------- |
| `package` | `Namespace` | EXACT |
| `module` (JPMS) | `Namespace` | CANONICAL |
| `class` | `NormalizedClass` | EXACT |
| `record` | `NormalizedClass` (with `is_record=True`) | CANONICAL |
| `interface` | `NormalizedInterface` | EXACT |
| `enum` | `NormalizedEnum` | EXACT |
| `@interface` (Annotation) | `NormalizedClass` (with `is_annotation=True`) | CANONICAL |
| `constructor` | `Constructor` | EXACT |
| `method` | `Method` | EXACT |
| `field` | `Field` | EXACT |
| `parameter` | `Parameter` | EXACT |

## Semantic / Relationship Mappings
| Java Construct | Canonical SDK SemanticFact | Confidence |
| -------------- | -------------------------- | ---------- |
| `import` | `DEPENDS_ON` (ImportFact) | EXACT |
| `extends` | `INHERITS_FROM` (InheritanceFact) | EXACT |
| `implements` | `IMPLEMENTS` (ImplementationFact) | EXACT |
| `throws` | `DEPENDS_ON` (DependencyFact) | CANONICAL |
| `@Annotation` usage | `ANNOTATED_AS` (AnnotationFact) | EXACT |
| `new Object()` | `INSTANTIATES` (ExecutionFact) | EXACT |
| `public`/`private`/`protected` | `HAS_VISIBILITY` (VisibilityFact) | EXACT |

## Generics Mappings
| Java Construct | Canonical SDK Abstraction | Confidence |
| -------------- | ------------------------- | ---------- |
| `<T>` | `GenericParameter` | EXACT |
| `extends T` (bound) | `GenericBound` | EXACT |
| `?` (wildcard) | `GenericWildcard` | CANONICAL |

## Execution Mappings
| Java Construct | Canonical SDK Abstraction | Confidence |
| -------------- | ------------------------- | ---------- |
| `try-catch` | `ExceptionHandling` | EXACT |
| `Lambda () -> {}` | `AnonymousFunction` | EXACT |
| `Method Reference (::)` | `FunctionReference` | EXACT |

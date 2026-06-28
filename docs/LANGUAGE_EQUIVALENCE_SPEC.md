# Language Equivalence Specification

This document defines the canonical engineering mappings for the OSEF Language Processing Platform v1. 

It is the absolute certification contract for every future language pack. If a concept exists in this table, the language plugin **must** map it to the specified OSEF `SemanticFact` and resulting `GraphDelta` ontology, regardless of the underlying syntax.

## Structural Mappings

| Concept | TypeScript | Java | Go | Rust | OSEF Canonical Output |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Class** | `class` | `class` | `struct` | `struct` | `Software.Class` |
| **Interface** | `interface` | `interface` | `interface` | `trait` | `Software.Interface` |
| **Enumeration** | `enum` | `enum` | `const + iota` | `enum` | `Software.Enum` |
| **Namespace** | `namespace`/`module` | `package` | `package` | `module` | `Software.Namespace` |
| **Generic** | `<T>` | `<T>` | `[T any]` | `<T>` | `Software.GenericParameter` |
| **Method** | `method` | `method` | `func (recv)` | `fn (self)` | `Software.Method` |

## Relational Mappings (SemanticFacts)

| Language Relationship | TypeScript Example | Java Example | Go Example | OSEF SemanticFact |
| :--- | :--- | :--- | :--- | :--- |
| **Inheritance** | `extends Base` | `extends Base` | *Composition* | `INHERITS` |
| **Implementation**| `implements IFace` | `implements IFace` | *Implicit* | `IMPLEMENTS` |
| **Importing** | `import {X}` | `import X;` | `import "X"` | `DEPENDS_ON` |
| **Ownership** | nested classes | nested classes | struct methods | `OWNS` |
| **Execution** | `func()` | `func()` | `func()` | `EXECUTES` |
| **Type Usage** | `x: Type` | `Type x` | `x Type` | `HAS_TYPE` |

## Metadata Mappings

| Concept | TypeScript | Java | Go | Rust | OSEF Property |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Visibility** | `public`/`private` | `public`/`private` | Upper/Lower case | `pub` | `is_public` |
| **Annotation** | `@Decorator` | `@Annotation` | Struct Tags | `#[macro]` | `has_annotation` |
| **Constant** | `const` | `final` | `const` | `const` | `is_constant` |

> **Certification Rule:** Any language pack that requires an alteration to this spec to function has failed the abstraction proof. SDK extensions are forbidden for language-specific idiosyncrasies.

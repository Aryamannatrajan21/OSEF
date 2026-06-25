# OSEF Engineering Ontology Specification (EOS)

## Version 1.0

### Purpose

The Engineering Ontology Specification (EOS) defines the canonical vocabulary, entities, relationships, and lifecycle of the Open Source Engineering Framework (OSEF).

EOS is the semantic foundation of OSEF.

Every subsystem—including the Engineering Knowledge Kernel, CLI, SDK, Plugin System, AI Agents, Documentation Engine, Prompt Engine, and future integrations—must use the terminology defined here.

The ontology exists to eliminate ambiguity and establish a common language for humans and AI.

---

# Fundamental Philosophy

OSEF models engineering knowledge rather than code.

Everything in OSEF is either:

* Knowledge
* Behavior
* Interface
* Artifact
* Execution
* Extension

No component exists outside one of these categories.

---

# Layer 1 — Foundational Concepts

## Engineering Knowledge

The canonical representation of engineering expertise.

Examples:

* Principles
* Standards
* Patterns
* Best Practices
* Anti-Patterns
* RFCs
* ADRs
* Playbooks
* Templates
* Checklists

Knowledge is immutable in intent but versioned in implementation.

Knowledge is the source of truth.

---

## Capability

A reusable engineering function.

Examples:

Repository Analysis

Architecture Review

Security Audit

Documentation Generation

Release Planning

Governance Validation

Testing Review

A Capability describes **what** OSEF can do.

It does not define **how** it is implemented.

---

## Service

A runtime implementation of one or more Capabilities.

Examples:

Architecture Service

Knowledge Service

Template Service

Prompt Service

Validation Service

Repository Service

Services expose stable interfaces.

---

## Artifact

A tangible engineering output.

Examples:

README

PRD

SRS

RFC

ADR

Architecture Diagram

Test Report

Release Notes

Changelog

Roadmap

Artifacts are versioned.

Artifacts may reference Knowledge.

Artifacts are produced by Capabilities.

---

## Resource

Any external or internal asset consumed by OSEF.

Examples:

Markdown

YAML

JSON

Templates

Configuration

Repositories

Source Code

Documentation

Images

Schemas

---

# Layer 2 — Runtime Concepts

## Agent

An autonomous reasoning component.

Responsibilities:

Planning

Reviewing

Generating

Validating

Explaining

Researching

An Agent performs reasoning.

An Agent does not own engineering knowledge.

Agents consume the Engineering Knowledge Kernel.

---

## Workflow

An ordered sequence of engineering activities.

Example:

Repository

↓

Analyze

↓

Architecture Review

↓

Documentation Review

↓

Security Review

↓

Validation

↓

Report

Workflows coordinate multiple capabilities.

---

## Task

A unit of work executed during a Workflow.

Examples:

Generate README

Review Architecture

Validate Documentation

Load Knowledge

Tasks are transient.

---

## Session

The execution context for a user interaction.

Contains:

Project

Configuration

Active Plugins

Loaded Knowledge

Memory

Selected AI Provider

History

Sessions isolate execution state.

---

# Layer 3 — Extension Concepts

## Plugin

An independently installable extension that contributes one or more Capabilities.

A Plugin may register:

Commands

Templates

Knowledge

Validators

Generators

Reviewers

Agents

Schemas

Configuration

Plugins never modify Core directly.

Plugins extend Core through stable interfaces.

---

## Extension Point

A documented location where Plugins may integrate.

Examples:

Command Registration

Knowledge Registration

Prompt Registration

Validation Hooks

Lifecycle Hooks

Template Providers

Storage Providers

---

## Hook

A specific lifecycle callback.

Examples:

BeforeProjectInit

AfterProjectInit

BeforeValidation

AfterValidation

BeforeDocumentation

AfterDocumentation

Plugins subscribe to Hooks.

---

# Layer 4 — Knowledge Concepts

## Engineering Knowledge Kernel (EKK)

The authoritative repository of engineering knowledge.

Stores:

Principles

Patterns

Standards

Architecture

Governance

Playbooks

Examples

Lessons

Templates

RFCs

ADRs

Relationships

The EKK never executes engineering work.

It only provides authoritative knowledge.

---

## Knowledge Item

The smallest independently versioned unit of engineering knowledge.

Examples:

SOLID

Semantic Versioning

Repository Layout Standard

Plugin Design Pattern

Testing Checklist

Each Knowledge Item has:

Unique ID

Version

Category

Relationships

Metadata

Lifecycle

Validation Status

---

## Knowledge Domain

A logical collection of related Knowledge Items.

Examples:

Architecture

Security

Testing

Documentation

Python

DevOps

Governance

Release Engineering

---

## Knowledge Relationship

Defines semantic connections.

Relationship Types:

DependsOn

Extends

Implements

References

Supersedes

Contradicts

InspiredBy

Requires

Recommends

Validates

Uses

Generates

Relationships are directional and version-aware.

---

# Layer 5 — Interaction Concepts

## Prompt

A dynamically assembled instruction for an AI model.

Prompts are generated from Knowledge.

Prompts never contain canonical engineering rules.

The Prompt Engine composes prompts at runtime.

---

## Prompt Template

A reusable blueprint for Prompt generation.

Templates contain variables.

Templates consume Knowledge.

Templates remain AI-provider neutral.

---

## Context

The information supplied to an AI model.

May include:

Project

Knowledge

Memory

Artifacts

Configuration

User Request

Repository Analysis

Contexts are generated automatically.

---

# Layer 6 — Project Concepts

## Project

A software initiative managed by OSEF.

Contains:

Repository

Configuration

Artifacts

Knowledge References

Plugins

History

Workflows

---

## Repository

A version-controlled codebase.

Contains:

Source

Documentation

Configuration

History

Tests

Metadata

OSEF analyzes repositories.

OSEF does not own repositories.

---

## Module

A cohesive implementation unit within a Project.

Modules expose Interfaces.

Modules contain Components.

---

## Component

The smallest architectural implementation unit.

Components implement Interfaces.

Components are replaceable.

---

# Layer 7 — Governance Concepts

## RFC

A proposal describing a possible future engineering decision.

RFCs may be:

Draft

Review

Accepted

Rejected

Superseded

RFCs do not modify architecture.

---

## ADR

A permanent record of an accepted architectural decision.

ADRs explain:

Decision

Rationale

Alternatives

Consequences

References

ADRs are part of institutional memory.

---

## Principle

A rule that guides engineering decisions.

Examples:

Documentation First

Architecture Before Code

Plugin First

Configuration Over Hardcoding

Principles rarely change.

---

## Standard

A measurable engineering requirement.

Examples:

Naming

Formatting

Testing

Documentation

Standards are enforceable.

---

## Policy

A governance rule.

Policies describe organizational behavior.

Policies differ from engineering standards.

---

# Layer 8 — Platform Concepts

## Core

The minimal permanent runtime of OSEF.

Core owns:

Configuration

Plugin Manager

Knowledge Kernel

Event Bus

Dependency Injection

Logging

Lifecycle

Everything else should be extensible.

---

## SDK

The official programmatic interface.

The SDK exposes stable APIs.

Third-party tools should depend on the SDK rather than internal modules.

---

## CLI

The primary user-facing interface.

The CLI invokes Capabilities.

The CLI contains no engineering knowledge.

---

# Canonical Relationships

Engineering Knowledge
defines
Principles

Principles
guide
Decisions

RFC
proposes
Decisions

ADR
records
Decisions

Knowledge
powers
Capabilities

Capabilities
are implemented by
Services

Services
expose
Interfaces

Interfaces
are consumed by
CLI
SDK
Plugins
Agents

Plugins
contribute
Capabilities

Agents
orchestrate
Workflows

Workflows
execute
Tasks

Tasks
produce
Artifacts

Artifacts
reference
Knowledge

Repositories
contain
Projects

Projects
contain
Modules

Modules
contain
Components

Components
implement
Interfaces

---

# Naming Rules

Every concept in OSEF must have exactly one canonical definition.

Avoid synonyms.

Examples:

Use "Capability", never "Feature" unless referring to user-visible functionality.

Use "Knowledge Item", never "Document" unless describing a concrete artifact.

Use "Artifact" for generated outputs.

Use "Service" for implementations.

Use "Interface" for contracts.

Use "Plugin" for extensions.

Use "Agent" for autonomous reasoning.

This vocabulary is mandatory across documentation, code, prompts, SDKs, and AI-generated output.

---

# Evolution Rules

The ontology is versioned.

Breaking changes require:

* An RFC.
* An approved ADR.
* Documentation updates.
* Migration guidance.
* Version increment.

No subsystem may redefine ontology terms independently.

The EOS is the semantic contract of OSEF.

---

# Final Principle

Every contribution to OSEF must answer two questions before implementation:

1. **Which ontology concepts does this affect?**
2. **Does it introduce a new concept that truly belongs in the ontology, or can it be expressed using existing concepts?**

The ontology should remain small, precise, and stable.

Engineering knowledge evolves through refinement, not through uncontrolled growth of terminology.

# OSEF AI Executive Context

**READ THIS FILE BEFORE EXECUTING ANY COMMANDS OR WRITING CODE.**

## Project Summary
OSEF is the Engineering Operating System for AI-assisted software development. It parses source code into an immutable **Engineering Knowledge Graph (EKG)**, executes rules via the **Engineering Policy Engine (EPE)**, and exposes a decoupled **Engineering Platform SDK (EPSDK)** for extensibility. 

### 2. Execution Runtime
The OSEF runtime architecture is **FROZEN**.
- **PipelineEngine** orchestrates stages.
- **ExtensionHost** discovers capabilities.
- **CapabilityRegistry** resolves stateless providers.
- **EventBus** purely observes.
Any deviation requires a formal RFC and ADR.

### 3. Modus Operandi
- All new language support requires a dedicated Parser Capability.
- Go and TypeScript parsers have been formally prioritized for Q2.
- **Decision:** All parsers MUST implement the standard `ParserContract` (v0.4.0+).

## Current State
- **Current Version:** `v0.4.0-alpha`
- **Current Sprint:** Sprint 5 - Ecosystem Validation
- **Current Release:** v0.4.0 (EPSDK Release)
- **Current Architecture:** EPSDK-driven Plugin Ecosystem
- **Frozen Components:** Scanner, Parser Contracts, EKG, EPE, EPSDK (Extension Host/Context). 

## Immediate Context
- **Current Goal:** Establish Reference Plugin Ecosystem and validate Marketplace Protocol.
- **Immediate Next Step:** See `.osef/NEXT_SESSION.md`.
- **Current Risks:** CI fragmentation if plugins do not strictly adhere to capabilities negotiation.
- **Top Technical Debt:** No Go or TypeScript parsers yet; CLI error reporting is minimal.

## Things Never To Change
1. Never bypass the `ExtensionContext`.
2. Never mutate the EKG.
3. Never reverse architectural decoupling. 
4. Never assume—refer to documentation and the repository state.

---

## 🚨 MANDATORY STARTUP PROTOCOL 🚨
Every AI Assistant **MUST** execute the following reads upon starting a session:

1. Read `.osef/AI_CONTEXT.md` (You are here)
2. Read `.osef/PROJECT_STATE.md`
3. Read `.osef/NEXT_SESSION.md`
4. Read `.osef/VERSION_STATE.md`
5. Read `.osef/ARCHITECTURE_STATE.md`
6. Read `.osef/ROADMAP_STATE.md`
7. Read `.osef/DECISIONS.md`
8. Read `.osef/TECH_DEBT.md`
9. Read `.osef/KNOWN_LIMITATIONS.md`
10. Read `.osef/ARCHITECTURE_GUARDRAILS.md`

**Do NOT begin implementation until this sequence is complete.**

*Last Updated: Sprint 4 Closeout*

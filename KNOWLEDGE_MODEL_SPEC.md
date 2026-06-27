# OSEF Knowledge Model Specification

The Engineering Knowledge Graph (EKG) is built from composed **Knowledge Domains**. 

This document is the canonical index of every recognized knowledge model in OSEF.

## Core Tenet
Every Knowledge Domain follows a strict, repeatable architecture:
`Knowledge Model -> Adapters -> GraphDelta -> Policies -> Projections -> Dashboards -> CLI -> Certification`

## 1. Software Knowledge Model (Core)
The foundational structural model of source code.
- **Node Types**: `Software.Service`, `Software.Package`, `Software.Class`, `Software.Function`, `Software.Interface`, `Software.Dependency`
- **Adapters**: Python (Reference), Language Packs (Planned)

## 2. Documentation Knowledge Model
The contextual model of engineering documentation.
- **Node Types**: `Documentation.README`, `Documentation.Architecture`, `Documentation.API`, `Documentation.Runbook`, `Documentation.Decision`
- **Adapters**: Markdown

## 3. Infrastructure Knowledge Model (IKM)
The operational and deployment architecture model.
- **Node Types**: `Infrastructure.Service`, `Infrastructure.Container`, `Infrastructure.Node`, `Infrastructure.Deployment`, `Infrastructure.Volume`, `Infrastructure.Network`, `Infrastructure.Secret`
- **Adapters**: Docker, Compose, Kubernetes, Terraform (Planned), Helm (Planned)

## 4. Security Knowledge Model (SKM)
The model for vulnerabilities, exposure, and security posture.
- **Node Types**: `Security.Asset`, `Security.Boundary`, `Security.Risk`, `Security.Control`, `Security.Finding`, `Security.Policy`, `Security.Vulnerability`, `Security.Exposure`, `Security.Identity`, `Security.Secret`
- **Adapters**: Trivy, Bandit

## 5. Architecture Knowledge Model (AKM)
The semantic model of boundaries, layers, constraints, and intended design. It serves as the bridge between all domains.
- **Node Types**: `Architecture.Domain`, `Architecture.Layer`, `Architecture.Component`, `Architecture.Boundary`, `Architecture.Constraint`, `Architecture.Interface`, `Architecture.Dependency`, `Architecture.Decision`, `Architecture.Pattern`, `Architecture.View`, `Architecture.Module`
- **Adapters**: C4Model, OsefArchitecture, ADR, Structurizr, PlantUML, ArchiMate

## 6. Runtime Knowledge Model (⏳ Planned)
The runtime execution and telemetry model.

## 7. Enterprise Knowledge Model (⏳ Planned)
The organizational governance and compliance model.

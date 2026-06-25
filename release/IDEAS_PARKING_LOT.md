# OSEF Ideas Parking Lot

## Overview
This is the structured repository for ideas that are valuable but explicitly fall outside the `v1.0.0` MVP Boundary. Storing them here preserves the vision while protecting the current implementation focus.

---

### Idea 1: Distributed Runtime
- **Description:** Allow OSEF Event Bus to span multiple machines via Redis or NATS.
- **Motivation:** Enables enterprise-scale analysis across thousands of repositories simultaneously.
- **Priority:** Low
- **Estimated Complexity:** Extreme
- **Dependencies:** OSEF v1.0 Stability.
- **Potential Release:** v3.x
- **Reason for Deferral:** Violates MVP requirement for a simple, local-first runtime.

### Idea 2: Vector Search / Local Embeddings
- **Description:** Index codebase ASTs and EKK rules using local embedding models (e.g., `sentence-transformers`).
- **Motivation:** Allows semantic querying ("Are there any functions doing XYZ?").
- **Priority:** Medium
- **Estimated Complexity:** High
- **Dependencies:** Core OSTE Analysis stability.
- **Potential Release:** v2.x
- **Reason for Deferral:** Requires heavy dependencies (PyTorch/Transformers) which violates the Minimal Core principle. Better suited as a plugin.

### Idea 3: Autonomous GitHub Bot
- **Description:** An OSEF service that runs on GitHub Actions, automatically replying to PRs with architectural reviews.
- **Motivation:** Pushes OSEF directly into the review loop.
- **Priority:** High
- **Estimated Complexity:** Medium
- **Dependencies:** Certification Engine MVP.
- **Potential Release:** v1.x (Post-MVP)
- **Reason for Deferral:** Focus must remain on the core static analyzer first.

### Idea 4: Plugin Marketplace
- **Description:** A centralized registry for sharing and discovering OSEF plugins.
- **Motivation:** Ecosystem growth.
- **Priority:** Medium
- **Estimated Complexity:** High
- **Dependencies:** SDK and Plugin API stability.
- **Potential Release:** v2.x
- **Reason for Deferral:** Premature optimization. We must prove the plugin model works locally first.

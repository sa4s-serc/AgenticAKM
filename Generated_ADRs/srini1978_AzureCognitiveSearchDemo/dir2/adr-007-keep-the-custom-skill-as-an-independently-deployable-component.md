---
### ADR-007: Keep the custom skill as an independently deployable component

**Status:** Inferred
**Context:** The custom skill is packaged as its own Azure Functions project, separate from search index definitions and data plane code.
**Decision:** Decouple the custom skill from the search service configuration, deploying it as a standalone HTTP endpoint consumed by the skillset.
**Consequences:** 
- Positive: Loose coupling; reusability across multiple indexes or solutions; independent lifecycle and scaling.
- Negative: Additional operational surface area (deployment, monitoring, CI/CD) separate from the search service.
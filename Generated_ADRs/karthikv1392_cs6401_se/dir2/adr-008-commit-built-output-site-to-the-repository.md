---
### ADR-008: Commit built output (_site) to the repository

**Status:** Inferred
**Context:** A full _site directory with generated HTML and assets is present, which is typically excluded in Jekyll projects.
**Decision:** Include the generated site in version control, likely for distribution, archival, or alternative hosting.
**Consequences:**
- Positive: Instant offline access; stable snapshots for archival/release; easier mirroring without a build step.
- Negative: Repository bloat; risk of divergence between source and built output; potential merge conflicts on generated files.
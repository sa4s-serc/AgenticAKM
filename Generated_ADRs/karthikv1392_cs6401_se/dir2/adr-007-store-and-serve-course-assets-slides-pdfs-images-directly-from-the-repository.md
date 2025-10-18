---
### ADR-007: Store and serve course assets (slides, PDFs, images) directly from the repository

**Status:** Inferred
**Context:** The repository includes a slides directory with PDFs/PPTX, assets/images with many images, and _site/resources PDFs.
**Decision:** Commit binary course materials into the repo and serve them as static assets.
**Consequences:**
- Positive: Single source of truth; predictable URLs; offline availability via cloned repo; simplifies linking from pages.
- Negative: Increases repository size; binary files are not diff-friendly; potential for large history growth.
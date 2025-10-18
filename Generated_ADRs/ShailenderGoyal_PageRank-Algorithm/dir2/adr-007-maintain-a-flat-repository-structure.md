---
### ADR-007: Maintain a flat repository structure

**Status:** Inferred
**Context:** The repository lists only top-level files ("project.py", "README.md") and no nested source or configuration directories.
**Decision:** Keep a flat, minimal repository layout without additional directories.
**Consequences:** 
- Positive: Simplicity and ease of navigation for a small project.
- Negative: Limited scalability; as code and assets grow, organization, discoverability, and maintainability may degrade.
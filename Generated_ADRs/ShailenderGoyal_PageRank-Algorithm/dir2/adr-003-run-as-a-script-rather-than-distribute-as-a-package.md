---
### ADR-003: Run as a script rather than distribute as a package

**Status:** Inferred
**Context:** There are no packaging or build files (e.g., pyproject.toml, setup.py) and no defined entry points. This suggests the intended execution is via python project.py.
**Decision:** Provide the application as a directly runnable script instead of a packaged, installable distribution.
**Consequences:** 
- Positive: Quick start for users; no packaging overhead.
- Negative: Harder to version, distribute, or integrate as a library; cannot be installed via pip; path/ENV management left to users.
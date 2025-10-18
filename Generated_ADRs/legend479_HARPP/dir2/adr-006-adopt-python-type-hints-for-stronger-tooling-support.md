---
### ADR-006: Adopt Python type hints for stronger tooling support

**Status:** Inferred
**Context:** requirements.txt lists typing, and the project structure (domain modules and tests) benefits from static analysis and IDE assistance, particularly for geometry and composite structures.
**Decision:** Use Python type hints across modules to improve readability, developer tooling, and error detection.
**Consequences:** 
- Positive: Better IDE autocomplete, earlier detection of type-related issues, clearer contracts between modules.
- Negative: Additional developer effort to maintain annotations; potential friction with dynamic patterns.
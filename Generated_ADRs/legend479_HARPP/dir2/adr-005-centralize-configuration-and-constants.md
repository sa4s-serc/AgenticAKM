---
### ADR-005: Centralize configuration and constants

**Status:** Inferred
**Context:** The project includes constants.py, indicating a decision to avoid scattering magic numbers and string literals across the codebase.
**Decision:** Store configurable values and shared literals in constants.py to provide a single source of truth for UI settings, colors, dimensions, and other parameters.
**Consequences:** 
- Positive: Easier tuning and consistency, simplifies maintenance and refactoring.
- Negative: Risk of over-centralization or tight coupling if constants become a dumping ground; changes may have wide ripple effects.
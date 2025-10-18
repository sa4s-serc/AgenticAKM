---
### ADR-009: Use a custom minimal layout rather than an external theme

**Status:** Inferred
**Context:** Presence of _layouts/minimal.html and multiple custom SCSS partials, with no remote theme specified in the provided context.
**Decision:** Build and maintain a lightweight custom theme/layout tailored to the course’s needs.
**Consequences:**
- Positive: Full control over presentation; minimal dependencies; exact fit for course structure.
- Negative: More maintenance effort; fewer benefits from community theme updates or fixes.
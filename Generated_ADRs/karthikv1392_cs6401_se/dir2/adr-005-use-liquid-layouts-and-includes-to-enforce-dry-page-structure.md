---
### ADR-005: Use Liquid layouts and includes to enforce DRY page structure

**Status:** Inferred
**Context:** The repo contains _layouts (announcement.html, minimal.html, module.html, schedule.html, staffer.html) and _includes (head.html, minutes.liquid).
**Decision:** Centralize presentation logic via layouts and reusable includes for common components and page types.
**Consequences:**
- Positive: Consistent look-and-feel; simpler content files; easier global changes.
- Negative: Indirection can increase learning curve; template changes can have wide impact if not carefully validated.
---
### ADR-010: Organize lecture content as week-based pages under Lectures/

**Status:** Inferred
**Context:** Files like Lectures/week-1.md through Lectures/week-9.md indicate a week-indexed structure rather than blog-style posts.
**Decision:** Represent lectures as static pages grouped by week within a dedicated directory, with separate index/listing pages.
**Consequences:**
- Positive: Intuitive navigation for students; straightforward linking; stable URLs per week.
- Negative: Manual curation may be needed for indexes and navigation; fewer out-of-the-box features compared to using Jekyll posts (e.g., automatic chronology).
---
### ADR-006: Style the site with SCSS partials compiled by Jekyll

**Status:** Inferred
**Context:** The _sass/custom directory contains multiple SCSS partials (announcement.scss, card.scss, custom.scss, etc.).
**Decision:** Use Jekyll’s SCSS pipeline with modular partials to manage styling.
**Consequences:**
- Positive: Maintainable, modular styling; reuse across layouts; easier theming and incremental changes.
- Negative: Requires SCSS build step; contributors must be comfortable with SCSS conventions.
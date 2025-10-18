---
### ADR-004: Separate concerns with a standalone stylesheet

**Status:** Inferred
**Context:** The repository separates styling into style.css rather than inlining all styles or using CSS-in-JS. This promotes a clean separation of concerns.
**Decision:** Maintain styles in a dedicated style.css file referenced by index.html.
**Consequences:** 
- Positive: Improved readability, browser caching benefits for CSS, clearer separation between structure (HTML), behavior (JS), and presentation (CSS).
- Negative: Global CSS scope can lead to style leaks and specificity conflicts; no use of scoped CSS or preprocessors (e.g., Sass) to aid organization.
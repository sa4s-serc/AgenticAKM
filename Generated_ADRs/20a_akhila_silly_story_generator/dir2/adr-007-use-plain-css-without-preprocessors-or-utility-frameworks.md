---
### ADR-007: Use plain CSS without preprocessors or utility frameworks

**Status:** Inferred
**Context:** Only a single style.css is present, with no indicators of Sass/Less, PostCSS, or utility frameworks (e.g., Tailwind) or CSS libraries.
**Decision:** Write styling in standard CSS without preprocessors or external CSS frameworks.
**Consequences:** 
- Positive: No tooling required, smaller footprint, straightforward debugging.
- Negative: Fewer abstractions for variables/mixins, potential repetition, and more manual effort to enforce consistency and responsiveness as styles grow.
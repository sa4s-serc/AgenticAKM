---
### ADR-003: Avoid a build step and deliver raw assets

**Status:** Inferred
**Context:** No build tooling artifacts (e.g., package.json, webpack/rollup/vite configs, transpiled output) are present. Files appear to be served as-is.
**Decision:** Do not use bundlers, transpilers, or other build tools; serve index.html, index.js, and style.css directly.
**Consequences:** 
- Positive: Faster development feedback cycle, fewer moving parts, reduced tooling complexity.
- Negative: Limited use of modern language features that require transpilation, no bundling/treeshaking optimizations, potential challenges with modularization and cache-busting strategies.
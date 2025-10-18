---
### ADR-007: Use PropTypes for runtime prop validation instead of TypeScript

Status: Inferred
Context: prop-types is included; there is no TypeScript configuration or .ts/.tsx files.
Decision: Validate component props with PropTypes and rely on JavaScript + runtime checks rather than adopting TypeScript.
Consequences:
- Positive: Lower barrier to entry; no additional build tooling or type definitions; faster initial velocity.
- Negative: Misses compile-time type safety; potential for runtime errors that static typing could prevent; weaker developer tooling for refactors.
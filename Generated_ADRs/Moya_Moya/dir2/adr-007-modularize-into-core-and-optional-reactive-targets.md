---
### ADR-007: Modularize into core and optional reactive targets

**Status:** Inferred
**Context:** To avoid forcing reactive dependencies on all consumers, the codebase separates core and integrations. The Sources layout contains Moya (core), RxMoya, ReactiveMoya, and CombineMoya.
**Decision:** Keep core networking and abstractions in Moya; provide separate targets/frameworks for reactive wrappers.
**Consequences:** 
- Positive: Lean core; consumers only import what they need; clearer dependency boundaries.
- Negative: Multiple artifacts to release and document; potential version skew across modules.
- Trade-off: Clean separation of concerns vs. operational overhead.
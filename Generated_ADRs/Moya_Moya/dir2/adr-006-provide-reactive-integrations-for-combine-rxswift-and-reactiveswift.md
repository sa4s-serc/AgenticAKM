---
### ADR-006: Provide reactive integrations for Combine, RxSwift, and ReactiveSwift

**Status:** Inferred
**Context:** Different teams use different reactive ecosystems. The repository has dedicated modules and docs for Combine, RxSwift, and ReactiveSwift.
**Decision:** Ship optional modules: CombineMoya, RxMoya, and ReactiveMoya, exposing publishers/observables/signal producers for requests and responses.
**Consequences:** 
- Positive: Broad adoption; seamless integration with popular reactive frameworks; composable async patterns.
- Negative: Increased maintenance burden and build matrix; conditional dependencies.
- Trade-off: Wider ecosystem support at the cost of module complexity.
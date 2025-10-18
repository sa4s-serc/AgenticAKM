---
### ADR-010: Ensure thread-safety and cancellation semantics

**Status:** Inferred
**Context:** Networking work is concurrent; shared state and plugin callbacks must be safe. Files Atomic.swift and Cancellable.swift indicate concurrency considerations and cancellation support.
**Decision:** Use an Atomic utility where needed for synchronization; expose a Cancellable interface for in-flight request cancellation.
**Consequences:** 
- Positive: Safer concurrent behavior; predictable cancellation handling.
- Negative: Complexity around synchronization; possible performance cost from locking.
- Trade-off: Correctness and safety over minimal runtime overhead.
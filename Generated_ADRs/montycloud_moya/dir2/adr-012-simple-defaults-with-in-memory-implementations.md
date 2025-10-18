---
### ADR-012: Simple Defaults with In-Memory Implementations

Status: Inferred
Context: Developers need to get started quickly without external services. Production users may later swap components.
Decision: Provide in-memory default implementations for repositories and registries, with optional file-system persistence for memory.
Consequences:
- Positive: Fast local setup; low barrier to entry; good for tests and demos.
- Negative: Not suitable for scaling, durability, or concurrency; requires explicit migration to production-grade stores.
---
### ADR-009: Caching for Cost and Latency Reduction

Status: Inferred
Context: LM and embedding calls are expensive and slow; many workloads are repeated.
Decision: Introduce caching in clients (dspy/clients/cache.py) and utilities (dspy/utils/caching.py). Provide user-level configuration (docs include configure_cache).
Consequences:
- Positive: Reduced cost and latency; improved throughput in dev/test/CI.
- Negative: Cache invalidation complexity; potential staleness; need for configurable keys and storage backends.
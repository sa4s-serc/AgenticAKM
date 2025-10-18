---
### ADR-012: Concurrency and Async Orchestration

Status: Inferred
Context: Many LM and retrieval calls can be parallelized or benefit from async orchestration.
Decision: Provide utilities for async/sync bridging (asyncify, syncify), a parallelizer (utils/parallelizer.py), and prediction modules supporting parallelism (predict/parallel.py).
Consequences:
- Positive: Higher throughput; better resource utilization; improved latency for batch tasks.
- Negative: Increased complexity; potential race conditions; provider rate-limit coordination needed.
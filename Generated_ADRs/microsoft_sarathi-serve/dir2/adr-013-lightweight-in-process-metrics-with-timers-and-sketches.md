---
### ADR-013: Lightweight, in-process metrics with timers and sketches

Status: Inferred
Context: metrics/ includes cpu_timer.py, cuda_timer.py, cdf_sketch.py, metrics_store.py and readme guidance.
Decision: Implement a minimal metrics subsystem using CPU/GPU timers and CDF sketches to collect latency/throughput statistics without external dependencies.
Consequences:
- Positive: Low overhead instrumentation; works in offline/cluster environments; suitable for benchmarking loops.
- Negative: Less feature-rich than full observability stacks; limited aggregation/retention capabilities.
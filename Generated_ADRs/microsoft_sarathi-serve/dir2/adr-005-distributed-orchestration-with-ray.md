---
### ADR-005: Distributed orchestration with Ray

Status: Inferred
Context: Ray is a hard dependency (ray>=2.5.1). There are Ray utilities (engine/ray_utils.py, benchmark/capacity_search/ray_utils.py) and distributed components (worker, pipeline_parallel_worker).
Decision: Use Ray for process orchestration, scheduling, and distributed execution (including multi-node), leveraging Ray Data for benchmarking/traces (pandas/pyarrow dependencies).
Consequences:
- Positive: Simplifies scaling out; standardized remote execution; ease of deployment on Ray clusters.
- Negative: Runtime dependency on Ray; potential overhead vs. bespoke RPC; requires Ray-compatible packaging and cluster ops.
---
### ADR-004: Decouple scheduling and KV-cache management via Scheduler and BlockSpaceManager

Status: Inferred
Context: The core includes multiple schedulers (sarathi, vllm, orca, faster_transformer) and multiple block space managers mirroring those policies. KV cache/block allocation is a major constraint in LLM serving.
Decision: Introduce Scheduler and BlockSpaceManager abstractions that can be combined to implement different policies and memory management strategies, enabling comparisons and hybrid designs.
Consequences:
- Positive: Flexible policy experimentation; targeted optimizations per memory strategy; easier benchmarking across policies.
- Negative: Increased complexity of integration surfaces; more cross-component coordination and state management.
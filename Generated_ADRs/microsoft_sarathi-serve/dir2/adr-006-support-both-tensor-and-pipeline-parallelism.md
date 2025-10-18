---
### ADR-006: Support both tensor and pipeline parallelism

Status: Inferred
Context: parallel_utils includes tensor_parallel and pipeline_parallel submodules; dedicated pipeline_parallel_llm_engine and worker exist.
Decision: Provide first-class support for pipeline parallel and tensor parallel strategies, with mapping utilities to place model shards across devices/processes.
Consequences:
- Positive: Flexibility to optimize for different model sizes and hardware topologies; better resource utilization.
- Negative: Larger configuration and orchestration surface; more complex debugging and failure handling.
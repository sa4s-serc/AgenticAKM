---
### ADR-003: Distributed Computing Orchestration with Ray

**Status:** Inferred

**Context:** Modern LLMs are often too large to fit on a single GPU and require immense computational resources. To serve these models effectively, the system must support distributed inference across multiple GPUs and potentially multiple machine nodes. This involves complex challenges in model parallelization (both tensor and pipeline), worker management, inter-process communication, and fault tolerance.

**Decision:** The Ray framework was chosen to handle the distributed computing aspects of the system. The presence of `ray >= 2.5.1` in `requirements.txt`, alongside `ray_utils.py` files and modules for `pipeline_parallel` and `tensor_parallel` (e.g., `pipeline_parallel_llm_engine.py`, `pipeline_parallel_worker.py`), indicates that Ray's actor model is used to manage distributed workers and orchestrate the model execution graph.

**Consequences:**
*   **Positive:**
    *   Ray simplifies the development of distributed systems by abstracting away low-level process and network communication details.
    *   It provides a robust and scalable foundation for implementing complex parallelism strategies like tensor and pipeline parallelism.
    *   Ray's ecosystem includes tools that are leveraged for other tasks, such as the extensive `benchmark/capacity_search` functionality.
*   **Negative:**
    *   Introduces a significant dependency on the Ray framework, including its associated overhead and complexity.
    *   Debugging distributed applications within Ray can be more challenging than debugging a single-process application.
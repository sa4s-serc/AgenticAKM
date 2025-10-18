---
### ADR-002: Modular and Pluggable Scheduling and Memory Management

**Status:** Inferred

**Context:** Efficient LLM inference serving requires sophisticated strategies for managing incoming requests and GPU memory, particularly the KV cache. Different techniques exist (e.g., vLLM's PagedAttention, Orca's iteration-level scheduling), each with unique performance characteristics and trade-offs. A monolithic architecture would lock the system into a single strategy, making it difficult to experiment with new research or adapt to different workloads.

**Decision:** The system was designed with a modular core, abstracting the scheduling and memory management logic behind well-defined interfaces. This is evident from the directory structure `sarathi/core/`, which contains `scheduler` and `block_space_manager` sub-packages. Each of these contains a `base_*.py` defining the interface, multiple concrete implementations (e.g., `vllm_scheduler.py`, `orca_scheduler.py`, `sarathi_scheduler.py`), and a `*_registry.py` to dynamically select the desired policy at runtime. This employs the Strategy design pattern.

**Consequences:**
*   **Positive:**
    *   The system is highly extensible; new scheduling and memory management algorithms can be added with minimal changes to the core engine.
    *   Enables rigorous A/B testing and benchmarking of different state-of-the-art serving strategies.
    *   The system can be configured to use the optimal policy for a specific model, hardware, or traffic pattern.
*   **Negative:**
    *   The added layer of abstraction can increase code complexity and make the control flow harder to follow.
    *   Requires careful design of the base interfaces to accommodate a wide range of future strategies.
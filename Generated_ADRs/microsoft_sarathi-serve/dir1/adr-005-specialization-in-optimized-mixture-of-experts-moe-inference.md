---
### ADR-005: Specialization in Optimized Mixture-of-Experts (MoE) Inference

**Status:** Inferred

**Context:** Mixture-of-Experts (MoE) models like Mixtral represent the state-of-the-art in LLM performance but pose unique serving challenges. Their massive parameter counts and dynamic, token-level routing logic require highly optimized kernels and scheduling to avoid becoming communication- or memory-bound and to run inference efficiently.

**Decision:** The architecture is explicitly designed and optimized for serving MoE models. This is demonstrated by the significant investment in MoE-specific components: custom CUDA kernels for MoE operations (`csrc/moe_topk_softmax_kernels.cu`), a dedicated `fused_moe` Python layer (`sarathi/model_executor/layers/fused_moe/`), a native implementation for the `mixtral` model, and a large collection of hardware-specific tuning configurations for MoE layers on various GPUs (NVIDIA A100/H100, AMD MI300X).

**Consequences:**
*   **Positive:**
    *   The system is highly competitive for serving one of the most important and demanding classes of modern LLMs.
    *   The hardware-specific tuning and custom kernels likely provide a significant performance advantage over generic inference solutions for MoE models.
*   **Negative:**
    *   This specialization adds significant complexity to the codebase and maintenance burden.
    *   Performance may be tightly coupled to specific hardware architectures, requiring substantial effort to optimize for new hardware as it becomes available.
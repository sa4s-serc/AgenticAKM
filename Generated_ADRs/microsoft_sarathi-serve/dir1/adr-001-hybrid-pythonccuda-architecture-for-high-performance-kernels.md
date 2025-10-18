### ADR-001: Hybrid Python/C++/CUDA Architecture for High-Performance Kernels

**Status:** Inferred

**Context:** The primary goal of this software is to serve Large Language Models (LLMs) with high throughput and low latency. Standard Python and PyTorch implementations of certain performance-critical neural network operations, such as layer normalization, activations, and Mixture-of-Experts (MoE) gating, can become significant performance bottlenecks under heavy load. To achieve state-of-the-art performance, these operations need to be executed as efficiently as possible on the target hardware (GPUs).

**Decision:** A hybrid architecture was chosen. The high-level application logic, orchestration, and API layers are written in Python for ease of development and flexibility. However, performance-critical computational kernels are implemented in C++ and CUDA. These custom kernels are compiled into a shared library and integrated into the Python application as an extension, likely using Pybind11 or the native PyTorch C++ extension mechanism. This is evidenced by the `csrc` directory containing `.cpp` and `.cu` files (e.g., `layernorm_kernels.cu`, `moe_topk_softmax_kernels.cu`) alongside the `setup.py` and `ninja` dependency for building them.

**Consequences:**
*   **Positive:**
    *   Achieves significantly higher performance for key operations compared to pure Python/PyTorch equivalents by allowing fine-grained control over GPU resources.
    *   Enables the implementation of fused operations (e.g., "fused moe") that reduce memory bandwidth requirements and increase computational intensity.
    *   The Python control plane remains flexible and easy to iterate on.
*   **Negative:**
    *   Increases build complexity, requiring a C++/CUDA toolchain (`ninja`).
    *   Reduces portability, as the system is now tightly coupled to NVIDIA GPUs and the CUDA platform.
    *   The C++/CUDA code is more difficult to write, debug, and maintain than Python code.
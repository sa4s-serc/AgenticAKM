---
### ADR-003: Heterogeneous Hardware Acceleration on the Edge

**Status:** Inferred
**Context:** Edge devices vary widely in their hardware capabilities. To maximize performance and adoption, the edge client needs to run efficiently on a range of hardware, not just standard CPUs. The challenge is to support different hardware accelerators (like GPUs and NPUs) without creating completely separate versions of the application.
**Decision:** The edge client is designed to support multiple hardware backends, including CPU, GPU (NVIDIA), and NPU (Intel). This is evidenced by the specific requirements files (`requirements-edge-cpu.txt`, `requirements-edge-gpu.txt`, `requirements-edge-npu.txt`). The inclusion of the `openvino` and `optimum[openvino]` libraries specifically indicates a strategy to leverage Intel's OpenVINO toolkit to optimize and run models on Intel CPUs, integrated GPUs, and NPUs.
**Consequences:**
*   **Positive:**
    *   Maximizes performance by utilizing available hardware accelerators on edge devices.
    *   Provides significant deployment flexibility, allowing the application to run on a wide array of hardware.
    *   Future-proofs the edge client by allowing for the addition of new hardware backends.
*   **Negative:**
    *   Increases the complexity of dependency management, as shown by the multiple `requirements-*.txt` files and version constraints (e.g., for `numpy`, `networkx`).
    *   The testing matrix becomes much larger, requiring validation on each supported hardware type (`test_gpu.py`, `test_npu.py`).
    *   Requires developers to have expertise in multiple optimization toolkits (e.g., PyTorch for CUDA, OpenVINO for Intel).
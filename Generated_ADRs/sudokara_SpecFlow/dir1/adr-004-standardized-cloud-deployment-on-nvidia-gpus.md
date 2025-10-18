---
### ADR-004: Standardized Cloud Deployment on NVIDIA GPUs

**Status:** Inferred
**Context:** The cloud-side "target model" needs to be as powerful and accurate as possible to serve as the ground truth for the edge's speculative results. This requires a stable, high-performance, and standardized computing environment to ensure consistent behavior and simplify development and operations.
**Decision:** The cloud server deployment is standardized exclusively on NVIDIA GPUs using the CUDA platform. This is explicitly stated in the `requirements.txt` comments (`# For Cloud Server (CUDA GPU only)`). This decision is further supported by the presence of `install_cuda_pytorch.bat`, the dependency on `nvidia-ml-py3` for monitoring NVIDIA GPUs, and the general use of `torch` and `accelerate`, which have first-class support for CUDA.
**Consequences:**
*   **Positive:**
    *   Maximizes the performance and accuracy of the target model by leveraging a mature and powerful ML ecosystem (CUDA).
    *   Simplifies the cloud deployment and development process by targeting a single, well-defined hardware platform.
    *   Allows the team to take advantage of CUDA-specific optimizations.
*   **Negative:**
    *   Tightly couples the cloud infrastructure to a single hardware vendor (NVIDIA), leading to potential vendor lock-in.
    *   Incurs higher operational costs, as high-end NVIDIA GPUs are expensive.
    *   Limits deployment options for the cloud component to environments where NVIDIA GPUs are available.
---
### ADR-008: Support optional GPU acceleration via CUDA 11 pip wheels

Status: Inferred
Context: Python requirements include CUDA 11 runtime libraries and NVIDIA packages (e.g., nvidia-cuda-runtime-cu11, cudnn-cu11), without using a CUDA base image.
Decision: Include CUDA-enabled wheels for PyTorch and dependencies to opportunistically leverage GPUs when the runtime provides NVIDIA drivers and runtime.
Consequences:
- Positive: Single image can run on CPU or leverage GPU when available; avoids maintaining separate CPU/GPU images.
- Negative: Larger image size, longer installs; potential mismatches with host GPU/runtime; requires NVIDIA Container Runtime in production.
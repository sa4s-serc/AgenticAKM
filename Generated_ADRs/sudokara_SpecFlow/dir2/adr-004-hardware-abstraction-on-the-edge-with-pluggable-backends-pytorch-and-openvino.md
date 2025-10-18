---
### ADR-004: Hardware abstraction on the edge with pluggable backends (PyTorch and OpenVINO)

Status: Inferred
Context: Edge code includes edge/draft_model.py and edge/openvino_model.py. Requirements include openvino, openvino-dev, and optimum[openvino], alongside PyTorch. There are tests for GPU and NPU (test_gpu.py, test_npu.py).
Decision: Abstract edge inference behind interchangeable backends supporting CPU/GPU (PyTorch) and NPU (OpenVINO via Optimum).
Consequences:
- Positive: Broader hardware coverage; performance portability; easier experimentation with accelerators.
- Negative: Increased maintenance surface (multiple runtimes, conversion flows); dependency conflicts and version drift risk.
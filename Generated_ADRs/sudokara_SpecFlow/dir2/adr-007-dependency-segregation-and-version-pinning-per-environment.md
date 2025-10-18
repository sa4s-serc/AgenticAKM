---
### ADR-007: Dependency segregation and version pinning per environment

Status: Inferred
Context: Multiple requirements files: requirements-cloud.txt, requirements-edge*.txt, and a top-level requirements.txt with explicit notes and constraints (e.g., numpy<2.0.0, networkx<=3.1 for openvino-dev, pillow<11). Guidance to install PyTorch with CUDA first.
Decision: Maintain separate, constrained dependency sets for cloud and edge, with environment-specific pins to avoid conflicts and ensure accelerator compatibility.
Consequences:
- Positive: Reduces dependency hell; predictable builds; optimized footprints per environment.
- Negative: More files to maintain; risk of divergence; contributors must follow install order (e.g., CUDA wheels first).
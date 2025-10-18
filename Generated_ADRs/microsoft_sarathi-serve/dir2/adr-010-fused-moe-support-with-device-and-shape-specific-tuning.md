---
### ADR-010: Fused MoE support with device- and shape-specific tuning

Status: Inferred
Context: Dedicated fused MoE kernels (csrc/moe*.cu) and a Python layer (layers/fused_moe) use JSON configs keyed by device name, experts (E), and hidden sizes (N), including float8 variants.
Decision: Implement a fused MoE layer with externalized per-device/per-shape configuration to select optimal kernel parameters and block sizes at runtime.
Consequences:
- Positive: Significant speedups for MoE models (e.g., Mixtral); performance portability via table-driven tuning.
- Negative: Maintenance of a large configuration matrix; need for benchmarking to update/tune per hardware generation.
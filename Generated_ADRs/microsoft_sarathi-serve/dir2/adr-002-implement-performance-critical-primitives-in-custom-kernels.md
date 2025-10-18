---
### ADR-002: Implement performance-critical primitives in custom kernels

Status: Inferred
Context: Files such as csrc/activation_kernels.cu, csrc/layernorm_kernels.cu, csrc/moe_*.cu, csrc/pos_encoding_kernels.cu indicate bespoke kernels for common transformer operations and MoE routing/softmax.
Decision: Provide custom CUDA/C++ kernels for hot-path operations (activations, layer norm, positional encoding, MoE top-k softmax, block-size alignment) with Python bindings integrated under sarathi/model_executor/layers.
Consequences:
- Positive: Significant latency and throughput gains; control over memory access patterns and fusion strategies.
- Negative: Higher maintenance cost; need for extensive testing across devices/dtypes; dependency on CUDA toolchain.
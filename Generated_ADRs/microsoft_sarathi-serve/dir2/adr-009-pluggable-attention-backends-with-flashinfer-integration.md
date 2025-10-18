---
### ADR-009: Pluggable attention backends with FlashInfer integration

Status: Inferred
Context: attention/ includes base_attention_wrapper.py, flashinfer_attention_wrapper.py, no_op_attention_wrapper.py, plus dependency on flashinfer==0.1.5.
Decision: Abstract attention via a wrapper interface and integrate FlashInfer as a high-performance backend, with the ability to swap or disable via registry.
Consequences:
- Positive: Accelerated attention kernels; flexibility to adopt new backends or fall back when unsupported.
- Negative: Tight version coupling (FlashInfer + PyTorch/CUDA); potential feature gaps across backends.
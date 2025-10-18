### ADR-001: Adopt PyTorch 2.3 + Transformers with custom CUDA/C++ extensions and Ninja-based builds

Status: Inferred
Context: The repository centers on high-performance LLM inference/serving. It depends on torch==2.3 and transformers>=4.37.0, and contains substantial CUDA/C++ code under csrc/ (activation, layernorm, pos encoding, MoE, top-k softmax, reduction utilities). A fast build tool (ninja) is required in requirements.txt and packaging files (pyproject.toml, setup.py, MANIFEST.in) are present to compile native extensions.
Decision: Standardize on PyTorch 2.3 and Transformers as the core ML stack, and implement performance-critical primitives as custom CUDA/C++ extensions compiled via setuptools + Ninja.
Consequences: 
- Positive: Unlocks kernel-level optimizations; predictable binary compatibility via pinned versions; faster inference on GPUs.
- Negative: Tight coupling to specific PyTorch/FlashInfer versions; added build complexity and CI burden; portability considerations across GPU architectures.
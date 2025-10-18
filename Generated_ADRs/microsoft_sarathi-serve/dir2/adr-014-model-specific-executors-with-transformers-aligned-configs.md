---
### ADR-014: Model-specific executors with Transformers-aligned configs

Status: Inferred
Context: model_executor/models supports falcon, internlm, llama, mistral, mixtral, qwen, yi; transformers_utils provides per-model config shims and tokenizers; weight_utils and model_loader handle loading.
Decision: Provide per-family model adapters layered on top of Transformers configs and custom weight-loading, while standardizing tokenization (sentencepiece, tiktoken) and rotary embeddings.
Consequences:
- Positive: Broad model support; tailored performance/compatibility per family; reuse of HF ecosystem.
- Negative: Fragmentation across model variants; ongoing upkeep as upstream models evolve.
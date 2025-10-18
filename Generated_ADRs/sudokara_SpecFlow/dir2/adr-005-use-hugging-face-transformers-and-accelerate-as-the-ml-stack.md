---
### ADR-005: Use Hugging Face Transformers and Accelerate as the ML stack

Status: Inferred
Context: requirements include transformers, accelerate, tokenizers, datasets, evaluate. cloud/target_model.py and edge/draft_model.py imply model loading and inference patterns aligned with these libraries.
Decision: Standardize on Transformers for model definitions/tokenization and Accelerate for efficient device placement and execution.
Consequences:
- Positive: Rich model ecosystem; well-supported performance utilities; easier integration with OpenVINO through Optimum.
- Negative: Larger dependency footprint; need to track upstream API changes; careful CUDA version alignment required.
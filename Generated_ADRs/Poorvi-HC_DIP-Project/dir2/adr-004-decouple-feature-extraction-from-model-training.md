---
### ADR-004: Decouple feature extraction from model training

Status: Inferred
Context: The presence of extract_features.py alongside training scripts indicates a two-stage pipeline: feature extraction followed by model training.
Decision: Implement feature extraction as a separate step producing intermediate representations consumed by training scripts.
Consequences:
- Positive: Enables feature caching, reuse across models, and faster iteration during model tuning.
- Negative: Requires careful synchronization of feature versions with models; managing intermediate artifacts and data lineage can be error-prone.
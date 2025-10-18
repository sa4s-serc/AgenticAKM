---
### ADR-006: Introduce dataset randomization utilities to mitigate ordering bias

Status: Inferred
Context: The file shuffle_frames.py indicates explicit handling of frame order, likely to avoid sequential bias or to create randomized training splits.
Decision: Provide a utility to shuffle frames prior to training or evaluation.
Consequences:
- Positive: Reduces overfitting to temporal patterns; simplifies creation of randomized datasets/splits.
- Negative: May discard temporal dependencies important for reconstruction quality; reproducibility depends on consistent seeding and logging.
---
### ADR-007: Include a retrieval-based baseline via nearest-neighbor search

Status: Inferred
Context: The file find_closest2.py suggests a nearest-neighbor or similarity lookup approach as part of the method suite.
Decision: Implement a retrieval-based baseline (e.g., nearest-neighbor matching) for reconstruction and/or evaluation reference.
Consequences:
- Positive: Simple, interpretable baseline; useful sanity check and fallback when learning-based models underperform.
- Negative: Scalability and memory limitations on large datasets; performance sensitive to feature quality and distance metrics.
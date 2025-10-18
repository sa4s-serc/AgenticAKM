---
### ADR-011: Ensure determinism via random_state

**Status:** Inferred
**Context:** MLflow parameters include random_state, indicating reproducibility settings during training.
**Decision:** Set random_state for the estimator to produce reproducible results.
**Consequences:** 
- Positive: Comparable runs and consistent results, facilitating debugging and auditing.
- Negative: May conceal natural variance; when not carefully managed across all randomness sources (e.g., data splits), determinism may be incomplete.
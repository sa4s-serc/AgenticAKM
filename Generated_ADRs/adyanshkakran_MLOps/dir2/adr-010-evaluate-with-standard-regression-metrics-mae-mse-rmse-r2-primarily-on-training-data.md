---
### ADR-010: Evaluate with standard regression metrics (MAE, MSE, RMSE, R2), primarily on training data

**Status:** Inferred
**Context:** MLflow metrics logged include training_mean_absolute_error, training_mean_squared_error, training_root_mean_squared_error, training_r2_score, training_score.
**Decision:** Use standard regression metrics and log them to MLflow, focusing on training metrics out-of-the-box.
**Consequences:** 
- Positive: Familiar metrics enable quick performance assessment and comparison across runs.
- Negative: Training-only metrics risk overestimating performance; without explicit validation/test logging, generalization is unclear and overfitting may go undetected.
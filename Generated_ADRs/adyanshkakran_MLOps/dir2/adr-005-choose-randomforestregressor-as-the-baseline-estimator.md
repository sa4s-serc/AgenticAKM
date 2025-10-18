---
### ADR-005: Choose RandomForestRegressor as the baseline estimator

**Status:** Inferred
**Context:** MLflow runs log parameters such as n_estimators, max_depth, bootstrap, max_features—matching RandomForestRegressor hyperparameters—despite the folder name suggesting linear regression.
**Decision:** Use RandomForestRegressor as the primary regression model.
**Consequences:** 
- Positive: Strong baseline with minimal feature engineering, robust to non-linearities and outliers.
- Negative: Larger model size, slower inference than linear models, less interpretable; may overfit without careful tuning and validation.
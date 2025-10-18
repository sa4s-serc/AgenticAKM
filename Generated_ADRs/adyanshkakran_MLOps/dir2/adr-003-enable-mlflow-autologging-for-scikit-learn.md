---
### ADR-003: Enable MLflow autologging for scikit-learn

**Status:** Inferred
**Context:** MLflow run tags indicate mlflow.autologging is enabled and estimator.html artifacts are present, which are typical outputs of MLflow’s scikit-learn autolog.
**Decision:** Use MLflow autologging to automatically capture parameters, metrics, and model artifacts during training.
**Consequences:** 
- Positive: Minimal logging code, consistent capture across runs, automatic environment files (conda.yaml/python_env.yaml).
- Negative: Less granular control over exactly what gets logged; may log training-only metrics by default unless overridden.
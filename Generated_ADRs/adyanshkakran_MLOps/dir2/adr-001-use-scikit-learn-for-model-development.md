### ADR-001: Use scikit-learn for model development

**Status:** Inferred
**Context:** The repository contains a classic ML workflow with scripts for data handling, model training, evaluation, and persistence. Artifacts and parameters logged in MLflow correspond to scikit-learn estimators.
**Decision:** Adopt scikit-learn as the core ML library for building and training models.
**Consequences:** 
- Positive: Simple API, rich model zoo, fast prototyping, strong community support.
- Negative: Limited for large-scale distributed training; production deployment may require wrapping or exporting models to runtime-compatible formats.
---
### ADR-002: Adopt MLflow for experiment tracking and model packaging

**Status:** Inferred
**Context:** The project includes an mlruns directory with runs, metrics, parameters, artifacts (MLmodel, conda.yaml, requirements.txt), and tags reflecting MLflow usage.
**Decision:** Use MLflow to track experiments, log metrics/parameters, and package models.
**Consequences:** 
- Positive: Reproducibility, centralized experiment history, standardized model packaging with environment capture.
- Negative: Adds a runtime dependency; without a remote tracking server, collaboration is limited to local artifacts.
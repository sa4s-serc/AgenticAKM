---
### ADR-007: Pin dependency versions and capture runtime environment

**Status:** Inferred
**Context:** requirements.txt pins mlflow==2.3, scikit-learn==1.2.2, numpy==1.24.3, cloudpickle==2.2.1; MLflow artifacts include conda.yaml and python_env.yaml.
**Decision:** Pin library versions and use MLflow’s environment capture to ensure reproducible runs.
**Consequences:** 
- Positive: Strong reproducibility and consistent model behavior across environments.
- Negative: Slower updates to newer library versions; potential dependency conflicts over time.
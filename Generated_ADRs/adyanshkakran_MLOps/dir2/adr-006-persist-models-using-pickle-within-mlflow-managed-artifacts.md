---
### ADR-006: Persist models using pickle within MLflow-managed artifacts

**Status:** Inferred
**Context:** MLflow artifacts include model.pkl and MLmodel metadata; typical of MLflow’s sklearn flavor which serializes models via pickle/cloudpickle.
**Decision:** Serialize trained models to pickle and store them as MLflow artifacts.
**Consequences:** 
- Positive: Seamless integration with MLflow; easy load/save across runs.
- Negative: Pickle ties model loads to Python and library versions; potential security risks if loading untrusted artifacts.
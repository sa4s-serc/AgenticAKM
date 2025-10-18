---
### ADR-004: Modular pipeline structure (data, model, train, eval, save, pipeline)

**Status:** Inferred
**Context:** The repository exposes separate modules: data.py, model.py, train.py, eval.py, save.py, and pipeline.py, indicating a separation of concerns across the ML lifecycle.
**Decision:** Organize the codebase into modular components for data loading, model definition, training, evaluation, persistence, and orchestration.
**Consequences:** 
- Positive: Improves maintainability, testability, and readability; allows independent evolution of pipeline stages.
- Negative: Slightly higher initial overhead to wire components; requires disciplined interfaces between modules.
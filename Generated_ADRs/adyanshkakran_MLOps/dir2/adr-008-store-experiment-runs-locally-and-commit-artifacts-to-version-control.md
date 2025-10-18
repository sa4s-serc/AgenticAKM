---
### ADR-008: Store experiment runs locally and commit artifacts to version control

**Status:** Inferred
**Context:** The mlruns directory with multiple runs and large artifacts exists in the repository, implying local tracking and committed artifacts.
**Decision:** Use MLflow’s default local tracking and commit run artifacts to the repository.
**Consequences:** 
- Positive: Self-contained demo/reproducibility without external services; easy onboarding.
- Negative: Repository bloat from binary artifacts; limited scalability and collaboration compared to a remote MLflow tracking server.
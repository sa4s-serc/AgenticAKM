---
### ADR-009: Automate experiment runs with command.sh and version results by episode

Status: Inferred
Context: EcoMLS/command.sh exists; Results include multiple episodes (EcoMLS(ep02), ep03, ep04) and structured outputs per approach.
Decision: Provide a shell script to orchestrate runs and store results under versioned episode directories for reproducibility.
Consequences:
- Positive: Reproducible pipelines; traceable comparisons across runs; easy reruns.
- Negative: Shell-based orchestration may be brittle across environments; growing repository size due to stored artifacts.
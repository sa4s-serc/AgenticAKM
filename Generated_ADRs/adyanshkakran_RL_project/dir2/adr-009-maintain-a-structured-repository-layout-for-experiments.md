---
### ADR-009: Maintain a structured repository layout for experiments

Status: Inferred
Context: Dedicated directories for models/, logs/, rewards/, data/, and notebooks (normalize.ipynb). Multiple timestamped run folders and named artifacts exist.
Decision: Adopt a filesystem-based experiment organization with clear separation of data, models, logs, and outputs.
Consequences:
- Positive: Easier navigation and experiment management; supports batch runs and post-hoc analysis; reproducibility through explicit artifacts.
- Negative: Requires manual housekeeping; risk of drift in naming conventions; potential for disk bloat over time.
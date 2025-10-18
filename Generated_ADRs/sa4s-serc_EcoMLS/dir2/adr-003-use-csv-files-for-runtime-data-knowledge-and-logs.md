---
### ADR-003: Use CSV files for runtime data, knowledge, and logs

Status: Inferred
Context: Numerous CSVs exist for knowledge.csv, model.csv, monitor.csv, MAPEK_energy.csv, log.csv, and Results/*/*.csv. Notebooks read results, implying file-based data exchange.
Decision: Persist monitoring data, model metadata, knowledge, and logs as CSV files to support analysis and reproducible experiments.
Consequences:
- Positive: Human-readable, easy to ingest via Python and notebooks; low tooling overhead; good for offline analysis and versioning in git.
- Negative: Limited concurrency and transactional guarantees; potential performance issues at scale; manual schema evolution.
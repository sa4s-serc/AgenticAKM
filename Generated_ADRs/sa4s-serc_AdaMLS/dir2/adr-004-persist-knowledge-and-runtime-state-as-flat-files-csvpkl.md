---
### ADR-004: Persist knowledge and runtime state as flat files (CSV/PKL)

**Status:** Inferred
**Context:** Knowledge artifacts are stored as CSV and pickle files, with logs and monitoring outputs in CSV (e.g., monitor.csv, model.csv, log.csv). There is no evidence of a database or message bus.
**Decision:** Use CSV for logs, monitoring, and knowledge mappings; use pickle for trained SKMeans models and initial centers.
**Consequences:** 
- Positive: Maximizes portability, simplicity, and reproducibility; easy to inspect and version. 
- Negative: Limited concurrency, transactional integrity, and scalability; potential file I/O bottlenecks. 
- Trade-off: Chose simplicity for research/experimentation over production-grade persistence.
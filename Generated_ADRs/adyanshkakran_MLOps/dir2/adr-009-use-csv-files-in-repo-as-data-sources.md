---
### ADR-009: Use CSV files in-repo as data sources

**Status:** Inferred
**Context:** Data files (data.csv, test.csv) are stored under linear_regression/data/.
**Decision:** Keep training and test data as CSV files within the repository.
**Consequences:** 
- Positive: Simple, portable, no external data dependency; ideal for demos and small datasets.
- Negative: Not suitable for large-scale data; lacks data versioning and lineage beyond VCS.
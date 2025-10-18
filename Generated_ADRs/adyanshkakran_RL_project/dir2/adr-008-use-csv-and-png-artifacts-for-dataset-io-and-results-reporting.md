---
### ADR-008: Use CSV and PNG artifacts for dataset I/O and results reporting

Status: Inferred
Context: Market data provided as CSVs under data/; rewards and cumulative-reward outputs stored as CSV and PNG plots under rewards/sac/; stats.csv and stats_DDPG.csv exist.
Decision: Standardize on CSVs for input data and metrics logging, and generate PNG plots for quick visual analysis.
Consequences:
- Positive: Simple, tooling-agnostic format; easy inspection and integration with Pandas; facilitates reproducible analysis.
- Negative: Larger experiments produce many files; CSVs can be slow for very large datasets; lacks schema guarantees beyond conventions.
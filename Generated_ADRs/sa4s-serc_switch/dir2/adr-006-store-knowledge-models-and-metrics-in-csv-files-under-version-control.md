---
### ADR-006: Store knowledge, models, and metrics in CSV files under version control

Status: Inferred
Context: Multiple CSVs persist knowledge and metrics (e.g., NAVIE/knowledge.csv, naive_knowledge.csv, model.csv, metrics.csv; AdaMLs knowledge cluster CSVs).
Decision: Use flat CSV files in the repository as the knowledge base and for experiment artifacts, rather than a database.
Consequences:
- Positive: Simplicity, transparency, and easy diff/versioning; reproducible experiments; no external DB dependency.
- Negative: Limited concurrency and scalability; risk of data corruption with concurrent writes; more manual data lifecycle management.
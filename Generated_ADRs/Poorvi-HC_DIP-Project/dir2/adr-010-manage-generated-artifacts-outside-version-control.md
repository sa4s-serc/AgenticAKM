---
### ADR-010: Manage generated artifacts outside version control

Status: Inferred
Context: Presence of .gitignore implies intentional exclusion of derived data (e.g., features, models, shuffled datasets) and local artifacts from the repo.
Decision: Exclude generated files and large datasets from version control, keeping the repository lean.
Consequences:
- Positive: Smaller repository size, faster cloning and CI; reduces accidental commits of large or sensitive data.
- Negative: Requires external data management practices; reproducibility depends on clear instructions and stable data paths not visible in VCS.
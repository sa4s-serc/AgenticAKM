---
### ADR-013: No database; stateless API with file-backed state

Status: Inferred
Context: No DB driver dependencies; all persistence is via files in uploads/posters/video/final_output folders.
Decision: Operate without a database; treat the API as stateless, with artifacts persisted to disk.
Consequences:
- Positive: Simpler deployment; fewer services to manage.
- Negative: Harder to query/report; scaling across instances needs shared storage; lifecycle/cleanup policies must be implemented.
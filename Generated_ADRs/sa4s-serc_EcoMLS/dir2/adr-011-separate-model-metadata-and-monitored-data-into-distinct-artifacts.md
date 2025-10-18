---
### ADR-011: Separate model metadata and monitored data into distinct artifacts

Status: Inferred
Context: Presence of model.csv (model metadata), monitor.csv (runtime metrics), and knowledge.csv (aggregated knowledge).
Decision: Keep model metadata, monitored runtime data, and derived knowledge in separate CSV artifacts to clarify responsibilities and data lifecycle.
Consequences:
- Positive: Clear data boundaries; simplifies updates to each dataset; supports cleaner analysis.
- Negative: Requires coordination and consistency across files; potential duplication of fields.
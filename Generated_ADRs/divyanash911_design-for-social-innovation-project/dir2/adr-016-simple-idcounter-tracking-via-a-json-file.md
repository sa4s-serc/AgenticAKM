---
### ADR-016: Simple ID/counter tracking via a JSON file

Status: Inferred
Context: backend/counters.json exists alongside images and app code, suggesting file-based counters (e.g., for image naming or entity IDs).
Decision: Use a JSON file to persist simple counters on the server.
Consequences:
- Positive: Minimal implementation effort; no additional infrastructure.
- Negative: Not safe for concurrent access or multi-instance deployments; risk of corruption; should be migrated to DB-backed counters for scale.
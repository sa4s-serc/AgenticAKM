---
### ADR-008: Store uploaded images on the backend filesystem

Status: Inferred
Context: backend/images contains saved image files named by IDs; no object storage or DB blobs indicated.
Decision: Persist uploaded images to the server’s local filesystem under a designated directory.
Consequences:
- Positive: Simple to implement; low operational overhead initially.
- Negative: Does not scale horizontally without shared storage; backup and lifecycle management required; deployment portability constraints.
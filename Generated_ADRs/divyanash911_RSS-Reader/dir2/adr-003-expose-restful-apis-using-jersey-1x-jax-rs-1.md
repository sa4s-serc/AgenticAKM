---
### ADR-003: Expose RESTful APIs using Jersey 1.x (JAX-RS 1)

Status: Inferred
Context: The dependency com.sun.jersey:jersey appears at version 1.19.4, indicating the project’s REST stack selection.
Decision: Implement REST endpoints using Jersey 1.x (JAX-RS 1).
Consequences:
- Positive: Mature, well-known framework with broad adoption and documentation.
- Negative: JAX-RS 1 is functionally limited vs JAX-RS 2 (no standardized async, filters/interceptors less rich); modernization will require migration.
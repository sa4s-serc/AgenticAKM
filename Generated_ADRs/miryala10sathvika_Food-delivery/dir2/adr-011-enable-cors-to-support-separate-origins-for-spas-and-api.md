---
### ADR-011: Enable CORS to support separate origins for SPAs and API

Status: Inferred
Context: cors dependency; three separate apps imply different hosts/ports in dev/prod.
Decision: Use CORS middleware on the API to allow frontends to call the backend across origins.
Consequences:
- Positive: Unblocks local dev and independent deployments; straightforward configuration.
- Negative: Must restrict allowed origins/headers for security; misconfiguration can expose endpoints.
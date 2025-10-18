---
### ADR-007: Enable cross-origin requests with Flask-CORS

Status: Inferred
Context: Separate frontend and backend projects; Flask-CORS in requirements.
Decision: Configure CORS on the Flask API to allow the React dev/prod origins to access resources.
Consequences:
- Positive: Unblocks local development and independent hosting.
- Negative: Misconfiguration can introduce security risks; requires environment-specific origin whitelisting.
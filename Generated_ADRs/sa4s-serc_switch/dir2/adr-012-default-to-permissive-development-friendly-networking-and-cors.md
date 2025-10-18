---
### ADR-012: Default to permissive, development-friendly networking and CORS

Status: Inferred
Context: ELK runs with no auth on a public port; Flask-Cors and cors (Node) are dependencies; services expose 3000, 3001, 5000, 8089.
Decision: Optimize for local development by exposing services on well-known ports and enabling cross-origin access between UI and backend.
Consequences:
- Positive: Minimal friction in local dev and experimentation; easy integration between UI, backend, and ELK.
- Negative: Insecure defaults unsuitable for production; requires explicit hardening (authn/z, TLS, network policies) before deployment.
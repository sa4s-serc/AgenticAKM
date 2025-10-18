---
### ADR-005: Enable CORS to support cross-origin development

Status: Inferred
Context: The backend depends on cors and the frontend runs on a different port (5173) than the backend (3050), with Nginx at 3000.
Decision: Enable CORS in the backend to allow the SPA (when accessed directly via the Vite dev server) to call backend APIs.
Consequences:
- Positive: Smooth local development across services and ports.
- Negative: Must be carefully configured in production to avoid overly permissive policies.
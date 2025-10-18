---
### ADR-014: Development workflow uses Nodemon for API and Vite dev servers for SPAs

Status: Inferred
Context: backend scripts include "server": "nodemon server.js"; Vite dev scripts in both SPAs.
Decision: Use Nodemon for hot-reloading backend during development; use Vite dev servers for frontends.
Consequences:
- Positive: Fast inner loop; minimal tooling.
- Negative: Multiple dev servers to run/manage; must coordinate ports and CORS in dev.
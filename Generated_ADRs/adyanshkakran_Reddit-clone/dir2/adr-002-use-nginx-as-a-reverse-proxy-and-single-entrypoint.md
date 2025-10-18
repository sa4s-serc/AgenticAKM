---
### ADR-002: Use Nginx as a reverse proxy and single entrypoint

Status: Inferred
Context: The nginx service is present with a Dockerfile and default.conf, exposing port 3000 and depending on backend and frontend, indicating routing responsibility.
Decision: Place Nginx in front of the frontend and backend to act as a gateway, proxying requests to the Vite frontend (port 5173) and the Express backend (port 3050), and serving as the single external entrypoint (port 3000).
Consequences:
- Positive: Centralized routing, simpler client configuration, potential SPA routing support, ability to enforce cross-cutting concerns (headers, caching).
- Negative: Additional service to configure and maintain; misconfiguration can lead to routing or caching errors.
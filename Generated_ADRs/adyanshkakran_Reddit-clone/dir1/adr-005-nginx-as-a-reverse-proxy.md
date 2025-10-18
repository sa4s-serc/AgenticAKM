---
### ADR-005: Nginx as a Reverse Proxy

**Status:** Inferred
**Context:** With a decoupled architecture, incoming user traffic needs to be routed to the correct service. API requests (e.g., to `/api/*`) must go to the backend, while requests for the web application itself (e.g., `/`) must go to the frontend. This routing needs to be managed from a single entry point.
**Decision:** An Nginx container is used as a reverse proxy. The `docker-compose.yml` file shows that the `nginx` service depends on both `frontend` and `backend` and is the only service that exposes a public-facing port (port 80, mapped from host 3000). It acts as the single gateway for all incoming requests.
**Consequences:**
*   **Positive:**
    *   Presents a single, unified domain to the end-user, hiding the underlying multi-service complexity.
    *   Simplifies CORS configuration, as from the browser's perspective, all requests are same-origin.
    *   Nginx is highly performant and can be extended to handle SSL termination, load balancing, caching, and serving static assets.
*   **Negative:**
    *   Adds another component to the architecture that must be configured and maintained.
    *   The `nginx/default.conf` file becomes a critical piece of configuration for the application's routing to function correctly.
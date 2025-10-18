---
### ADR-011: Run Without an External Reverse Proxy

Status: Inferred
Context: The Dockerfile’s entrypoint starts Gunicorn directly on port 80; no Nginx/Traefik/Caddy is defined in docker-compose.yml.
Decision: Serve HTTP traffic directly from Gunicorn without a separate reverse proxy layer.
Consequences: Simplifies deployment and reduces moving parts. Loses out-of-the-box TLS termination, advanced routing, and efficient static file serving that proxies provide. Production hardening (TLS, HSTS, caching) would require additional configuration or future introduction of a proxy.
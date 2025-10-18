---
### ADR-002: Serve the App with Gunicorn

Status: Inferred
Context: The Dockerfile’s entrypoint starts the app with gunicorn binding to 0.0.0.0:80. A production-grade WSGI server is necessary to run Flask in non-development environments.
Decision: Use Gunicorn as the WSGI HTTP server for the Flask application.
Consequences: Gunicorn offers robustness and concurrency management via workers, suitable for production. Without an external reverse proxy, TLS termination, request buffering, advanced routing, and static offloading must be addressed separately or within the app configuration.
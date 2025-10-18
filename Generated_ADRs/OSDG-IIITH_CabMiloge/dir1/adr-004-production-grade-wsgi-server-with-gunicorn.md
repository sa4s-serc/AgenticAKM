---
### ADR-004: Production-Grade WSGI Server with Gunicorn

**Status:** Inferred
**Context:** The default development server included with Flask is not suitable for production environments because it is single-threaded and lacks the robustness and performance features needed to handle concurrent users.
**Decision:** Gunicorn is used as the Web Server Gateway Interface (WSGI) HTTP server to run the Flask application. This is explicitly defined as the `ENTRYPOINT` in the application's `Dockerfile`: `ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:80", "app:app" ]`.
**Consequences:**
*   **Positive:**
    *   Provides a production-ready server capable of handling multiple concurrent requests through its worker management system.
    *   Improves the application's performance, stability, and reliability over the built-in Flask server.
    *   Decouples the application from the web server, a standard best practice.
*   **Negative:**
    *   Adds another dependency to the project stack.
    *   Requires some configuration (e.g., number of workers, timeouts) to be tuned for optimal performance, although the current setup uses simple defaults.
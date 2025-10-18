---
### ADR-013: Build a server-rendered Flask frontend with SQLite-backed user data

Status: Inferred
Context: frontend/app.py with Jinja2 templates, a users.db file, and pinned Flask/WTForms dependencies indicate a server-side rendered UI with simple local persistence.
Decision: Implement the UI using Flask templates and store user data in SQLite.
Consequences:
- Positive: Simple stack; low latency for rendering; minimal frontend build tooling.
- Negative: Limited scalability and concurrency for auth data; harder to adopt SPA patterns; eventual need to migrate to a central auth/DB.
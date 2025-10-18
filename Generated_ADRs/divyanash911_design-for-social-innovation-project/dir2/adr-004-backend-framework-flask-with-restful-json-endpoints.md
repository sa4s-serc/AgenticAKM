---
### ADR-004: Backend framework: Flask with RESTful JSON endpoints

Status: Inferred
Context: code/backend/app.py with Flask, Flask-CORS; requirements list Flask-related packages.
Decision: Implement the backend using Flask to expose REST-like JSON endpoints for authentication, questionnaires, responses, and analytics.
Consequences:
- Positive: Lightweight, quick to implement, large ecosystem.
- Negative: Requires manual structure/enforcement of best practices; fewer batteries-included features than larger frameworks (e.g., Django, FastAPI).
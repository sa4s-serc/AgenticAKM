### ADR-001: Adopt Flask as the Web Framework

Status: Inferred
Context: The repository contains a Python web application (app.py) with Jinja2 templates and static assets. The requirements pin Flask 3.x and related packages (Werkzeug, Jinja2, ItsDangerous), suggesting a lightweight, server-rendered web app suited to rapid development and straightforward hosting.
Decision: Use Flask as the primary web framework for building the cab sharing application.
Consequences: Flask provides simplicity, flexibility, and a small footprint, enabling quick iteration and easy deployment. However, it lacks batteries-included components (ORM, admin, auth), so additional libraries or custom code are needed for those concerns.
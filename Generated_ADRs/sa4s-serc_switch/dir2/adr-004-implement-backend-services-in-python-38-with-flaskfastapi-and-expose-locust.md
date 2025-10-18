---
### ADR-004: Implement backend services in Python 3.8 with Flask/FastAPI and expose Locust

Status: Inferred
Context: NAVIE Dockerfile uses python:3.8-slim-buster, requirements include Flask, Flask-Cors, FastAPI, Uvicorn, and Locust; ports 3001, 5000, and 8089 are exposed; entrypoint is Node.py.
Decision: Build a Python backend that can serve HTTP APIs (Flask and/or FastAPI), and expose Locust’s web UI (8089) for load generation and testing.
Consequences:
- Positive: Flexibility to choose API framework per need; built-in load testing harness; clear separation of concerns via ports.
- Negative: Increased complexity managing multiple frameworks and ports; potential duplication or confusion if both frameworks coexist.
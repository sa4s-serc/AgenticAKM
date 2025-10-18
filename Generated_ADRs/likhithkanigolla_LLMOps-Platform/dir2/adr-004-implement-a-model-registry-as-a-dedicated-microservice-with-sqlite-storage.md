---
### ADR-004: Implement a Model Registry as a dedicated microservice with SQLite storage

Status: Inferred
Context: model-registry/model-registry.py with config.py and a local model_registry.db file; requirements include Flask, Flask-Cors, python-dotenv, psutil, requests.
Decision: Provide a model registry as a standalone service persisting to SQLite.
Consequences:
- Positive: Simple, lightweight, zero-ops storage; easy local development.
- Negative: SQLite limits concurrency and horizontal scale; migrating to a networked RDBMS will require refactoring and data migration.
---
### ADR-002: Use FastAPI + Uvicorn for the API Gateway

Status: Inferred
Context: api-gateway/server.py exists alongside a requirements set including fastapi, uvicorn, pydantic, python-multipart, and dotenv. This indicates the gateway is performance-oriented and schema-driven at the edge.
Decision: Implement the API Gateway with FastAPI running on Uvicorn, using Pydantic for request/response models.
Consequences:
- Positive: High performance I/O, strong typing and validation, good developer ergonomics for public APIs.
- Negative: Mixed frameworks (FastAPI at the edge, Flask elsewhere) introduce cognitive overhead and duplicated patterns.
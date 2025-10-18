---
### ADR-002: FastAPI + Uvicorn as the backend web framework

Status: Inferred
Context: backend/requirements.txt includes fastapi[standard], uvicorn[standard]; backend/app.py suggests a FastAPI application serving multiple features (LLM, uploads, media generation).
Decision: Implement the backend as a FastAPI app served by Uvicorn.
Consequences:
- Positive: Async I/O support, good performance, built-in OpenAPI, easy request validation with Pydantic.
- Negative: Requires careful async handling with CPU-bound workloads (media rendering); operational familiarity vs more common Flask/Django stacks.
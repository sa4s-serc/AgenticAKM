---
### ADR-007: Provide OpenAI-compatible serving via FastAPI/Uvicorn

Status: Inferred
Context: entrypoints/openai contains protocol and serving handlers (serving_chat.py, serving_completion.py), with FastAPI and Uvicorn in requirements; api_server.py exists.
Decision: Expose an OpenAI API-compatible HTTP interface built on FastAPI/Uvicorn for easy client interoperability.
Consequences:
- Positive: Drop-in compatibility with common tooling and SDKs; rapid adoption.
- Negative: Must track OpenAI API changes; potential impedance mismatch with internal features.
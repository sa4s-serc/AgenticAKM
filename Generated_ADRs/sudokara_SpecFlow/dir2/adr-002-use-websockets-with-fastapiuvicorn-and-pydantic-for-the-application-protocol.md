---
### ADR-002: Use WebSockets with FastAPI/Uvicorn and Pydantic for the application protocol

Status: Inferred
Context: Dependencies include fastapi, uvicorn, websockets, and pydantic. There is a common/protocol.py module, indicating shared message models and protocol definitions across edge and cloud. Real-time token exchange benefits from bi-directional low-latency communication.
Decision: Implement a real-time, bi-directional protocol over WebSockets hosted by FastAPI/Uvicorn, with Pydantic (v2) models for message validation, shared via common/protocol.py.
Consequences:
- Positive: Low-latency streaming suitable for token-level speculative decoding; strong schema validation and shared types reduce integration bugs.
- Negative: More complex connection lifecycle (reconnects, backpressure) versus simple HTTP; requires careful versioning of schemas across components.
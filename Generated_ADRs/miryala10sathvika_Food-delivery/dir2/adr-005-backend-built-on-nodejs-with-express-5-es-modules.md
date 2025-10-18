---
### ADR-005: Backend built on Node.js with Express 5 (ES Modules)

Status: Inferred
Context: backend/package.json sets "type": "module"; express ^5.1.0 is used; server.js as entry; routers/controllers per domain.
Decision: Use Express 5 with ES Modules for the HTTP API.
Consequences:
- Positive: Latest Express features; broad ecosystem; ESM aligns with modern Node.
- Negative: Some middleware and libraries still show CJS interop quirks; Express 5 changes may require migration considerations.
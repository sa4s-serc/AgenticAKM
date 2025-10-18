---
### ADR-003: RESTful HTTP APIs with multipart uploads

Status: Inferred
Context: python-multipart is included; frontend/src/utils/api.ts and components indicate fetch-based calls; no WebSocket or SSE code present.
Decision: Expose functionality over REST endpoints; use multipart for PDF and media uploads.
Consequences:
- Positive: Simple integration from browser; broadly compatible; easy caching/proxying.
- Negative: No real-time updates; long-running jobs may need polling or separate orchestration.
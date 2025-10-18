---
### ADR-010: Real-time features via WebSockets (Socket.IO)

Status: Inferred
Context: lib/startup/registerWebsocketEvents.ts and frontend/src/app/Services/socket-io.service.ts are present.
Decision: Integrate Socket.IO for real-time notifications and interactions.
Consequences:
- Positive: Better UX for live updates (e.g., notifications, scoreboard).
- Negative: Adds operational and security surface area; requires scaling strategies for WS connections.
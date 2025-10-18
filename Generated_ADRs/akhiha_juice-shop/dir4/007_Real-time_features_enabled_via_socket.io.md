# ADR-007: Real-time features enabled via socket.io

**Date**: 2025-10-10
**Status**: Proposed

## Context
Some challenges and UX elements benefit from server push and event-driven interactions.

## Decision
Integrate socket.io for WebSocket-style real-time communication between server and client.

## Consequences
Benefits: richer interactive challenges and notifications. Drawbacks: more complex CORS/session handling, additional vulnerability surface for websocket-specific issues, higher resource usage under load.
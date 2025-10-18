# ADR-003: JSON-over-HTTP API between frontend and backend

**Date**: 2025-10-13
**Status**: Proposed

## Context
The frontend includes axios and a clear separation between React and Flask services.

## Decision
Communicate between the React SPA and Flask backend using JSON over HTTP via axios calls from the client.

## Consequences
Decouples client and server for independent evolution and testing, but introduces network latency, versioning needs, and CORS/security considerations.
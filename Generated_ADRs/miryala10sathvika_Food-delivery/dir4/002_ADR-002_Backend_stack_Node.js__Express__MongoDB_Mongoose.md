# ADR-002: ADR-002: Backend stack: Node.js + Express + MongoDB (Mongoose)

**Date**: 2025-10-13
**Status**: Proposed

## Context
The backend uses Express (server.js), connects to MongoDB via config/db.js, and models are implemented with Mongoose under models/. Routes and controllers are separated.

## Decision
Standardize the backend on Express with Mongoose, following the current layered structure (routes → controllers → models). Keep config/db.js as the single connection module and maintain middleware for cross-cutting concerns.

## Consequences
- Familiar, lightweight stack enabling quick iteration.
- MongoDB schema flexibility via Mongoose; must enforce validation at model and controller layers.
- Add centralized error handling middleware and request validation to improve robustness.
- No immediate need for an ORM/SQL layer; switching databases would require significant rework.
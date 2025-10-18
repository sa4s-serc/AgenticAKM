# ADR-010: JWT-based authentication with password hashing

**Date**: 2025-10-16
**Status**: Proposed

## Context
The platform requires stateless auth for API access across front-end clients.

## Decision
Use JWT tokens for authentication and bcrypt/bcryptjs for password hashing.

## Consequences
Scales across stateless servers and simple to integrate with SPA; token revocation, rotation, and refresh flows must be designed; careful secret storage and token TTLs are critical.
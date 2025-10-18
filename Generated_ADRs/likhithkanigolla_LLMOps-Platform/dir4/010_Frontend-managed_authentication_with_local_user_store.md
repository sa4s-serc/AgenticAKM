# ADR-010: Frontend-managed authentication with local user store

**Date**: 2025-10-09
**Status**: Proposed

## Context
frontend/ contains login/registration templates and a local users.db file; no external identity provider integration is visible.

## Decision
Implement authentication directly in the frontend service with user data stored in a local SQLite database.

## Consequences
Pros: quick to implement, self-contained, minimal dependencies. Cons: weak security posture for multi-instance deployments, no SSO/OAuth/OIDC, potential session management pitfalls, and challenges with horizontal scaling and compliance.
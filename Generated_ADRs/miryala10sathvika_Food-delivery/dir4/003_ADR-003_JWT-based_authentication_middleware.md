# ADR-003: ADR-003: JWT-based authentication middleware

**Date**: 2025-10-13
**Status**: Proposed

## Context
An authentication middleware exists at backend/middleware/auth.js. JWT usage is inferred by naming and typical structure, but not explicitly confirmed by the tree.

## Decision
Formalize stateless authentication using JWT. Acceptance criteria: auth.js verifies JWTs signed with HS256 using process.env.JWT_SECRET; rejects expired/invalid tokens; attaches the decoded user to req.user; protects restricted routes. Verify existing middleware/auth.js meets these criteria; if not, implement or refactor accordingly.

## Consequences
- Backend remains stateless and horizontally scalable.
- Requires strong JWT_SECRET management and rotation (see ADR-010).
- Clients must store and send tokens (Authorization: Bearer <token> or HTTP-only cookie).
- Define token TTL and consider refresh-token flow later if needed.
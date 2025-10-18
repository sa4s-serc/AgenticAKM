# ADR-004: Stateless, Token-Based Authentication (JWT)

**Date**: 2025-10-14
**Status**: Proposed

## Context
A secure and scalable authentication mechanism was required to manage user sessions between the stateless frontend SPA and the backend API, without relying on server-side session storage.

## Decision
A token-based authentication system using JSON Web Tokens (JWT) was implemented. The backend generates a signed JWT upon successful login, which the client then includes in the headers of subsequent API requests. Passwords are securely hashed using bcrypt.

## Consequences
This stateless approach enhances scalability, as any backend instance can validate the token without needing access to a central session store. It decouples authentication from the API, making it easy to support other clients (e.g., mobile apps) in the future. A key consideration is that JWTs cannot be easily invalidated before their expiration, requiring alternative strategies like token denylists for immediate session termination.
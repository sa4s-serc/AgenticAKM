# ADR-005: Stateless JWT-Based Authentication

**Date**: 2025-10-16
**Status**: Proposed

## Context
A secure and scalable method was needed to manage user sessions and protect API endpoints, especially within a decoupled SPA and API architecture.

## Decision
JSON Web Tokens (JWT) are used for authentication. The server generates a token upon successful login, which the client then includes in the headers of subsequent requests to authenticated endpoints. Passwords are securely hashed using bcrypt.

## Consequences
JWT provides a stateless authentication mechanism, which is ideal for scalable, distributed systems as the server does not need to store session state. It works seamlessly with SPAs and mobile clients. The main consideration is the need for a robust token invalidation strategy (e.g., using blocklists) for events like user logout or password changes.
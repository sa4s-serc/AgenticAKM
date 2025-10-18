# ADR-004: Stateless API Authentication with JSON Web Tokens (JWT)

**Date**: 2025-10-13
**Status**: Proposed

## Context
In a decoupled architecture where the frontend and backend are separate applications, a secure and stateless mechanism was required to authenticate users and authorize access to protected API endpoints.

## Decision
The system implements stateless authentication using JSON Web Tokens (JWT). The backend API issues a signed token to a user upon successful login, which the client-side application then includes in the authorization header of all subsequent requests.

## Consequences
Using JWT eliminates the need for the server to maintain session state, which simplifies the architecture and makes it easier to scale the backend horizontally. It is a well-established standard for securing APIs in a microservices or decoupled environment. Passwords are also securely hashed using bcrypt before storage, protecting user credentials.
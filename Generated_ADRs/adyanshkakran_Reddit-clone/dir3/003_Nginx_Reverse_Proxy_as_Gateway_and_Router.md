# ADR-003: Nginx Reverse Proxy as Gateway and Router

**Date**: 2025-10-14
**Status**: Proposed

## Context
A single, unified entry point was needed to direct incoming user traffic. The system had to differentiate between API calls destined for the backend and requests for the web application's static assets.

## Decision
An Nginx container was configured as a reverse proxy. It serves as the application's sole entry point, routing traffic prefixed with `/api/` to the Node.js backend service, while serving the static, compiled React application for all other requests.

## Consequences
This effectively decouples the client from the server's location and port, simplifying network configuration and enabling CORS-free API communication. Nginx efficiently handles serving static files, offloading that work from the Node.js application server. This pattern also provides a natural point for future implementations of load balancing, SSL termination, and caching.
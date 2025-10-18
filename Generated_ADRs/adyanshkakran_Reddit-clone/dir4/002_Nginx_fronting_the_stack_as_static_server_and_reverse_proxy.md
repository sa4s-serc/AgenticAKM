# ADR-002: Nginx fronting the stack as static server and reverse proxy

**Date**: 2025-10-14
**Status**: Proposed

## Context
An nginx/ directory with default.conf and a Dockerfile is present, coordinated via docker-compose.

## Decision
Place Nginx in front of the application to serve built frontend assets and reverse proxy API requests to the Node/Express backend.

## Consequences
Enables single-origin deployment, improved caching and static delivery, and SPA routing support; adds configuration complexity, requires careful path routing to the API, and coordination when backend routes change.
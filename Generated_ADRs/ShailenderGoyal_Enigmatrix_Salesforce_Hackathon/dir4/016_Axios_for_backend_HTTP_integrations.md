# ADR-016: Axios for backend HTTP integrations

**Date**: 2025-10-16
**Status**: Proposed

## Context
The server depends on Axios for external HTTP calls (e.g., AI providers).

## Decision
Use Axios for outbound HTTP with standardized interceptors and timeouts.

## Consequences
Consistent request/response handling and easier retries; must configure timeouts and circuit breakers to protect the event loop; error normalization across providers is needed.
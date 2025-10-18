# ADR-001: Uniform Python/Flask microservices architecture

**Date**: 2025-10-09
**Status**: Proposed

## Context
Each service directory contains a single Python entrypoint (e.g., frontend/app.py, controller-Service/controller.py, deployer-service/server.py, api-gateway/server.py, reverse-proxy/reverse-proxy.py) with per-service requirements.txt files, matching a lightweight Flask-style microservice pattern.

## Decision
Adopt a microservices architecture implemented in Python, with each service as a small Flask-like server or agent exposing its own process and dependencies.

## Consequences
Pros: clear service boundaries, rapid iteration in a familiar stack, independent dependency management. Cons: operational overhead for many processes, duplicated cross-cutting concerns (auth, logging, metrics), inter-service latency, and higher complexity for observability and debugging.
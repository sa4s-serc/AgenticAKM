# ADR-001: Multi-Service Containerized Architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project required a clear separation of concerns between the user interface, business logic, and request handling to facilitate independent development, deployment, and scaling. A consistent environment was needed to minimize discrepancies between development and production.

## Decision
The application was architected as three distinct, containerized services (React Frontend, Node.js Backend, Nginx Proxy), orchestrated via Docker and Docker Compose. This creates a decoupled system where each component runs in its own isolated environment.

## Consequences
This approach enhances modularity and scalability, as each service can be updated and scaled independently. It provides a portable and reproducible environment, simplifying setup for new developers and deployments. The trade-off is a slight increase in initial setup complexity and resource overhead compared to a single monolithic application.
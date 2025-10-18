# ADR-004: Deployment and Environment Strategy

**Date**: 2025-10-14
**Status**: Proposed

## Context
To ensure consistency, portability, and ease of setup across development, testing, and production environments, a standardized deployment strategy was required.

## Decision
The entire application stack, including the Flask application, WSGI server, and a database management tool, is containerized using Docker and orchestrated via Docker Compose.

## Consequences
This decision ensures a highly portable and reproducible environment, eliminating 'it works on my machine' problems and simplifying the on-boarding of new developers. It makes deployment to any host with a Docker runtime trivial. The minor trade-off is the learning curve for developers unfamiliar with containerization, but the long-term benefits in consistency and reliability are substantial.
# ADR-006: OpenAPI-first API contract served via Swagger UI

**Date**: 2025-10-10
**Status**: Proposed

## Context
Learners and automated tests need discoverable, stable API documentation.

## Decision
Maintain swagger.yml and serve it through swagger-ui-express as part of the application.

## Consequences
Benefits: self-service API discovery and testing, easier client scaffolding and API test coverage. Drawbacks: risk of documentation drift from implementation, Swagger endpoint must be gated appropriately in certain modes.
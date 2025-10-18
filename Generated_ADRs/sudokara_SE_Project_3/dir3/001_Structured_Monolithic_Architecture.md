# ADR-001: Structured Monolithic Architecture

**Date**: 2025-10-14
**Status**: Proposed

## Context
The primary architectural style for the system needed to be chosen. The options included microservices, which offer scalability but add operational complexity, or a monolith, which is simpler to deploy but can become difficult to maintain. The goal was to balance ease of deployment with long-term maintainability.

## Decision
A 'Structured Monolith' architecture was deliberately chosen and documented in an ADR. The entire system is a single deployable unit, but its internal structure is highly modular with a clear separation of concerns (Observation, Compression/Encryption, Uploader, CLI).

## Consequences
This decision simplifies the deployment and operational overhead compared to a microservices architecture. The strong internal modularity mitigates common monolithic drawbacks by promoting a clean, maintainable codebase and allowing for the potential future extraction of modules into separate services if required.
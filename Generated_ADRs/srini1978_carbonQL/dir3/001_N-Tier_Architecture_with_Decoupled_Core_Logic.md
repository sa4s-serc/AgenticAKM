# ADR-001: N-Tier Architecture with Decoupled Core Logic

**Date**: 2025-10-09
**Status**: Proposed

## Context
The system required a clear separation between the user interface and the core calculation logic to promote reusability, testability, and the ability to support different client applications in the future.

## Decision
The solution was structured into two distinct projects: a `carbonQLBackend` class library containing all business logic and models, and a `carbonQLConsole` application acting as the presentation layer. A strict unidirectional dependency from the console to the backend was enforced.

## Consequences
This design makes the core logic highly portable and reusable, allowing new clients (e.g., a Web API, GUI) to be developed without modifying the backend. It simplifies isolated unit testing of the business logic and improves overall maintainability.
# ADR-002: Core Architectural Pattern

**Date**: 2025-10-16
**Status**: Proposed

## Context
To ensure maintainability, testability, and a clear separation of concerns, a well-defined architectural structure was necessary for the application.

## Decision
A classic three-tier layered architecture was implemented, distinctly separating the Presentation (Controller), Service (Business Logic), and Data Access (Repository/DAO) layers.

## Consequences
This structure results in a highly modular and decoupled codebase. It allows for independent development and testing of each layer (e.g., testing business logic without the web layer). This enhances long-term maintainability and makes the system easier to understand and scale.
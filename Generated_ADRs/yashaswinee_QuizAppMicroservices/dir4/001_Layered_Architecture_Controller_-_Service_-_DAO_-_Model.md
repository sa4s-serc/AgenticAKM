# ADR-001: Layered Architecture (Controller -> Service -> DAO -> Model)

**Date**: 2025-10-16
**Status**: Proposed

## Context
The application manages questions and quizzes with REST endpoints and backend persistence, requiring separation of HTTP concerns, business logic, and data access.

## Decision
Adopt a classic layered architecture with controllers handling HTTP, services encapsulating business rules, DAOs providing data access, and models representing domain entities.

## Consequences
Improves testability, maintainability, and clear ownership of responsibilities; enables swapping data access or business rules with minimal ripple effects, but adds boilerplate and increases the number of moving parts.
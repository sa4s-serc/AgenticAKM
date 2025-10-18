# ADR-003: MVC-Inspired Pattern for Backend Organization

**Date**: 2025-10-09
**Status**: Proposed

## Context
Within the core logic library, there was a need to organize data structures and the operations that act upon them in a structured and understandable way, even for a non-web application.

## Decision
The `carbonQLBackend` library was internally organized using folders named `Model` for data structures and `Controller` for business logic and calculations, drawing inspiration from common MVC/API patterns.

## Consequences
This structure enhances code readability and maintainability by clearly separating data representation from the logic that manipulates it. It provides a familiar pattern for developers, accelerating onboarding and ensuring a consistent internal design.
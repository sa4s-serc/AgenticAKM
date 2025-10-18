# ADR-004: State management with custom hooks per view

**Date**: 2025-10-10
**Status**: Proposed

## Context
useHomeFetch and useMovieFetch own fetching, loading/error flags, and pagination for their respective views.

## Decision
Leverage React custom hooks to encapsulate side effects and local view state instead of introducing a global state library.

## Consequences
Lightweight and composable state logic with clear ownership; duplication of patterns across views can emerge and cross-cutting concerns (e.g., global cache, analytics) are harder to centralize.
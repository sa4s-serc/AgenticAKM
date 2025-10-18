# ADR-001: State Management with Co-located Custom Hooks

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application required a strategy to manage asynchronous data, including loading and error states, particularly for view-specific data like movie lists and details. The goal was to avoid the complexity and boilerplate of a global state management library for state that was not globally shared.

## Decision
The architecture eschews a global state library (e.g., Redux) in favor of custom React Hooks (`useHomeFetch`, `useMovieFetch`). This pattern co-locates state management and data-fetching logic directly with the views that consume the data.

## Consequences
This results in a simpler, more maintainable architecture where logic is highly readable and scoped. It reduces boilerplate code and makes components more self-contained. The primary trade-off is that sharing state between deeply nested or unrelated components becomes more complex, potentially requiring prop drilling or the later addition of the Context API.
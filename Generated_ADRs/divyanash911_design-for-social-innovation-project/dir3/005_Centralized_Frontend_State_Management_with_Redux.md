# ADR-005: Centralized Frontend State Management with Redux

**Date**: 2025-10-13
**Status**: Proposed

## Context
The single-page application needs to manage a significant amount of shared and complex state, including user authentication status, questionnaire data, user responses, and analysis results, which must be consistent across various components and views.

## Decision
The Redux library was adopted for centralized state management. The application's global state is held in a single, immutable store, ensuring a predictable and traceable data flow throughout the component tree.

## Consequences
This approach provides a single source of truth for the application's state, making debugging easier and state changes predictable. It is highly scalable for a complex application. The trade-off is the introduction of boilerplate code (actions, reducers) and a steeper learning curve, which can increase development overhead for simpler features where React's native state management might suffice.
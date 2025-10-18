---
### ADR-004: Use React Context + reducer pattern for state management (instead of Redux)

Status: Inferred
Context: The presence of StateProvider.js and reducer.js indicates a custom context provider and reducer-based state handling. No Redux dependencies are present.
Decision: Manage app state with React Context and a reducer pattern to track cart, user session, and UI state.
Consequences:
- Positive: Minimal dependencies, simpler setup than Redux, fits small-to-medium complexity apps, colocated logic.
- Negative: Can become harder to scale and debug for complex state; potential re-render performance issues if not carefully memoized; fewer ecosystem tools compared to Redux.
---
### ADR-005: Manage server data with TanStack React Query; manage app state via React Contexts

Status: Inferred
Context: Dependencies include @tanstack/react-query and several contexts exist (AuthContext, LearningContext, ThemeContext). Components like ChatInterface and data utilities indicate frequent server communication.
Decision: Use React Query for server-state fetching/caching and React Context for cross-cutting client state (auth, learning, theming).
Consequences:
- Positive: Declarative data fetching, caching, retry/invalidation; simple global state without Redux.
- Negative: Requires discipline around query keys and invalidation; context can become coarse-grained if overused.
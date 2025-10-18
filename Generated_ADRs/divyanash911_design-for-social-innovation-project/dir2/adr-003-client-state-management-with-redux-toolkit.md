---
### ADR-003: Client state management with Redux Toolkit

Status: Inferred
Context: Dependencies include @reduxjs/toolkit and react-redux; reducers exist for questions and results in src/redux.
Decision: Use Redux Toolkit for application state (e.g., questionnaire state, results, UI flows).
Consequences:
- Positive: Predictable state management, good developer tooling, standardized patterns.
- Negative: Adds boilerplate and complexity versus lighter alternatives (Context, SWR, React Query) for simpler cases.
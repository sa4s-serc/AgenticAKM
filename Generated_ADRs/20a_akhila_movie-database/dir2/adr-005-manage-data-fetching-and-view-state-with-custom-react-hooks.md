---
### ADR-005: Manage data fetching and view state with custom React hooks

Status: Inferred
Context: src/hooks includes useHomeFetch.js and useMovieFetch.js. No Redux or other global state libraries are present.
Decision: Implement domain-specific custom hooks to encapsulate data fetching, caching logic, and component state.
Consequences:
- Positive: Lightweight state management tailored to feature needs; avoids Redux/Context complexity; improved reusability and testability of logic.
- Negative: Potential duplication across hooks if shared concerns grow; harder to inspect global state; may need refactoring if app complexity increases.
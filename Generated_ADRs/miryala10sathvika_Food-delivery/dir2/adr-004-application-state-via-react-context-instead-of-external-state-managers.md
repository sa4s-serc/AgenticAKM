---
### ADR-004: Application state via React Context instead of external state managers

Status: Inferred
Context: frontend/src/context/storeContext.jsx indicates use of React Context for cart and app state; no Redux/Zustand/MobX present.
Decision: Manage shared UI/app state with React Context and component state.
Consequences:
- Positive: Zero extra dependency; simple mental model; good for small-to-mid complexity.
- Negative: Re-renders can grow with app size; harder to optimize compared to dedicated state libraries; limited devtooling.
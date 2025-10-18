---
### ADR-004: Frontend State Management

**Status:** Inferred
**Context:** The React application is complex, with many shared states across different components. For example, user authentication status, questionnaire data, and user responses need to be accessed and modified from various parts of the UI (e.g., dashboards, question pages, navigation bar). Managing this state with React's built-in context or "prop drilling" would become cumbersome and error-prone.
**Decision:** Redux, specifically with `@reduxjs/toolkit`, was chosen for centralized state management. The presence of `react-redux`, `@reduxjs/toolkit`, a `src/redux/` directory containing `store.js`, `question_reducer.js`, and `result_reducer.js` confirms this decision.
**Consequences:**
*   **Positive:**
    *   Provides a single, predictable source of truth for the application's state, simplifying debugging and state tracking.
    *   Makes it easy for any component to access the global state without passing props down through many levels.
    *   Redux Toolkit simplifies Redux boilerplate, making it easier to write and maintain reducers and actions.
*   **Negative:**
    *   Adds a layer of abstraction and boilerplate, which can increase the learning curve for new developers.
    *   For simple state management needs, Redux can be overkill and add unnecessary complexity.
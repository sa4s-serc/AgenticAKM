---
### ADR-004: Client-Side State Management with React Context API

**Status:** Inferred

**Context:** A mechanism was needed to manage global application state, such as the current user's authentication status and the items in their shopping basket. This state needs to be accessible by many disparate components throughout the application without the complexity of "prop drilling" (passing props down through many layers of components).

**Decision:** The application uses React's built-in Context API, likely in combination with the `useReducer` hook, for global state management. This is inferred from the presence of `src/StateProvider.js` and `src/reducer.js`, which are common naming conventions for this pattern.

**Consequences:**
*   **Positive:**
    *   **No External Dependencies:** Avoids adding a large state management library like Redux, which keeps the application's bundle size smaller and reduces dependency overhead.
    *   **Simplicity:** The Context API is integrated into React and is generally considered easier to learn and implement for moderately complex state than Redux.
*   **Negative:**
    *   **Performance Concerns:** In large applications, the default behavior of the Context API can cause unnecessary re-renders in components that consume the context, potentially leading to performance issues.
    *   **Limited DevTools:** It lacks the advanced developer tooling, middleware support, and established patterns available in more mature state management libraries.
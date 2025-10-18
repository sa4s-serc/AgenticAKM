---
### ADR-004: State Management and Data Fetching Logic

**Status:** Inferred
**Context:** The application needs to fetch data from an external API and manage the associated state, including loading, error, and data states. This logic should be reusable and decoupled from the UI components to avoid code duplication and improve maintainability.
**Decision:** **Custom React Hooks** will be created to encapsulate and manage stateful logic, particularly for data fetching. The presence of `src/hooks/useHomeFetch.js` and `src/hooks/useMovieFetch.js` clearly indicates this pattern. This approach centralizes the logic for fetching and managing data for specific views.
**Consequences:**
*   **Positive:**
    *   **Reusability & Separation of Concerns:** Encapsulates complex logic, making it easy to reuse across multiple components and keeping presentational components clean and focused on rendering UI.
    *   **Improved Readability:** Components become more declarative by simply calling a hook (e.g., `const { state, loading, error } = useMovieFetch(movieId);`) rather than containing complex `useEffect` and `useState` implementations directly.
    *   **Follows Modern React Patterns:** Aligns with the official direction and best practices of the React library.
*   **Negative:**
    *   **Can Be Over-abstracted:** For very simple cases, creating a custom hook might be more boilerplate than necessary.
    *   **No Global State Management:** This approach is suited for local/component state. A separate solution would be needed if complex global state management (e.g., Redux, Zustand) were required.
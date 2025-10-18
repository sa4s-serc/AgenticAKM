---
### ADR-004: Implement a Multi-View User Interface

**Status:** Inferred
**Context:** The application has distinct functional areas: the main typing interface and a leaderboard display. To provide a clean user experience and maintain organized code, a decision was needed on how to structure the UI. Combining all functionality into a single, complex HTML file (a Single Page Application approach) could lead to tightly coupled code and a cluttered interface.
**Decision:** The UI was structured into multiple, separate views. This is evidenced by the existence of distinct sets of files for each view: `index.html` and `renderer.js` for the main application, and `leaderboard.html` and `leaderboard.js` for the leaderboard. This suggests either a multi-window approach or a single window that swaps between these HTML pages.
**Consequences:**
*   **Positive:**
    *   **Clear Separation of Concerns:** The code for each feature is neatly encapsulated in its own files, making it easier to understand, develop, and maintain independently.
    *   **Modularity:** UI components are self-contained, which can simplify the development workflow.
*   **Negative:**
    *   **State Management Complexity:** Sharing state or data between the different views (`index` and `leaderboard`) becomes more complex and requires explicit Inter-Process Communication (IPC) to pass information.
    *   **Navigation Logic:** Additional logic is required to manage the creation, display, and interaction between the different windows or views, which adds a small amount of overhead.
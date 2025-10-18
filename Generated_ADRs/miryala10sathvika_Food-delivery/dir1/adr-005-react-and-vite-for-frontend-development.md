---
### ADR-005: React and Vite for Frontend Development

**Status:** Inferred

**Context:** Two modern, responsive, and component-driven user interfaces were needed for the customer and admin applications. The tooling for building these interfaces needed to support a fast and efficient development workflow.

**Decision:** React was selected as the UI library for building the `frontend` and `admin` applications. This is confirmed by the presence of `.jsx` files and `react` dependencies. Vite was chosen as the build tool and development server, as indicated by `vite.config.js` and `@vitejs/plugin-react` in the `package.json` files.

**Consequences:**
*   **Positive:**
    *   React's component-based model encourages the creation of reusable and maintainable UI elements.
    *   Vite provides near-instant server start-up and extremely fast Hot Module Replacement (HMR), leading to a superior developer experience.
    *   There is a vast ecosystem of libraries and tools available for React, such as `react-router-dom` for routing, which is used in this project.
*   **Negative:**
    *   As a Single-Page Application (SPA), there may be challenges with initial page load performance and Search Engine Optimization (SEO) that require specific solutions (e.g., code splitting, server-side rendering).
    *   For global state management, the project appears to use React's built-in Context API (`frontend/src/context/storeContext.jsx`), which can become cumbersome for complex state interactions compared to dedicated libraries like Redux or Zustand.
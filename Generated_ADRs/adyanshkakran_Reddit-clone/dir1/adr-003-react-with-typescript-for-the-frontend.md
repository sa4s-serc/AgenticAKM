---
### ADR-003: React with TypeScript for the Frontend

**Status:** Inferred
**Context:** A modern, dynamic, and interactive user interface is required for the application. The codebase for this interface needs to be maintainable, scalable, and less prone to common JavaScript runtime errors.
**Decision:** The frontend is built as a Single-Page Application using the React library. TypeScript (`.tsx` files, `tsconfig.json`) is used instead of plain JavaScript to add static type-checking. Vite (`vite.config.ts`) is chosen as the build tool and development server.
**Consequences:**
*   **Positive:**
    *   React's component-based architecture promotes code reuse and maintainability.
    *   TypeScript catches type-related errors at compile time, improving code quality and developer confidence.
    *   Vite provides a very fast development experience with Hot Module Replacement (HMR).
    *   Client-side routing with `react-router-dom` enables a fluid user experience without full-page reloads.
*   **Negative:**
    *   Increased initial page load time compared to a server-rendered application.
    *   Search Engine Optimization (SEO) can be more challenging without server-side rendering (SSR) or static site generation (SSG) strategies.
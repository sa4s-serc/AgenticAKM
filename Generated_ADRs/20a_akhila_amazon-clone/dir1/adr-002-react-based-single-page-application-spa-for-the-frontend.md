---
### ADR-002: React-based Single-Page Application (SPA) for the Frontend

**Status:** Inferred

**Context:** The application required a modern, dynamic, and interactive user interface to provide a smooth e-commerce experience. A key challenge was to select a frontend technology that would allow for the creation of reusable UI components (like products, headers, and checkout forms) and efficient management of the UI state.

**Decision:** The frontend was built as a Single-Page Application (SPA) using the React library. The project was bootstrapped with `create-react-app`. Client-side navigation is managed by `react-router-dom`.

This decision is supported by the `package.json` file, which lists `react`, `react-dom`, `react-scripts`, and `react-router-dom` as core dependencies, and the `src/` directory structure, which is organized around React components.

**Consequences:**
*   **Positive:**
    *   **Component-Based Architecture:** Promotes reusability and maintainability of UI code.
    *   **Rich User Experience:** SPAs can provide a faster, more fluid user experience similar to a desktop application by updating a page's content dynamically without full reloads.
    *   **Strong Ecosystem:** React has a vast ecosystem of libraries, tools, and community support.
    *   **Simplified Tooling:** `create-react-app` handles the complex build configuration (Webpack, Babel), allowing developers to focus on application logic.
*   **Negative:**
    *   **SEO Complexity:** SPAs require specific techniques (like server-side rendering or pre-rendering) to be effectively indexed by search engines, which are not configured by default.
    *   **Initial Load Time:** The initial bundle size can be large, potentially leading to a longer first-page load time compared to a traditional multi-page application.
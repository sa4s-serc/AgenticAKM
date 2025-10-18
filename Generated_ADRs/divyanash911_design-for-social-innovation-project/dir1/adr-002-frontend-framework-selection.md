---
### ADR-002: Frontend Framework Selection

**Status:** Inferred
**Context:** A modern, component-based framework was needed to build a rich and interactive user interface. The application features multiple dashboards, forms, data visualizations, and complex user flows, necessitating efficient state management and a reusable component model.
**Decision:** React was chosen as the frontend JavaScript library. The project is bootstrapped using `create-react-app`, as indicated by the dependency on `react-scripts` and the standard file structure (`public/index.html`, `src/index.js`, `src/App.js`). The use of `react-router-dom` confirms the choice to build a Single Page Application (SPA) with client-side routing.
**Consequences:**
*   **Positive:**
    *   React's component-based architecture promotes reusability and maintainability, which is beneficial given the large number of components (`Card.js`, `Navbar.js`, multiple `Dashboard.js` files).
    *   A large ecosystem of libraries and tools is available, as shown by the inclusion of `react-chartjs-2`, `react-icons`, and `@reduxjs/toolkit`.
    *   Strong community support and a large talent pool make development and maintenance easier.
*   **Negative:**
    *   As an SPA, the initial load time might be longer than a server-rendered application.
    *   Search Engine Optimization (SEO) can be more challenging, though this may not be a primary concern for this type of dashboard-heavy application.
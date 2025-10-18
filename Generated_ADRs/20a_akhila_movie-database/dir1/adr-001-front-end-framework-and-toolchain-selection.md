### ADR-001: Front-end Framework and Toolchain Selection

**Status:** Inferred
**Context:** The project required a foundation for building a modern, interactive single-page application (SPA). Key challenges included managing UI state, creating a reusable component architecture, and configuring a robust development environment with features like live-reloading, code bundling, and production optimization without significant manual setup.
**Decision:** The project will be built as a **React Single-Page Application**, bootstrapped and managed by **Create React App (CRA)**. The presence of `react`, `react-dom`, and `react-scripts` in `package.json`, along with the standard `src/App.js` and `public/index.html` structure, confirms this choice.
**Consequences:**
*   **Positive:**
    *   **Rapid Development:** CRA provides a zero-configuration setup for a complete development toolchain (Webpack, Babel, Jest), significantly accelerating initial project setup.
    *   **Component-Based Architecture:** React facilitates the creation of encapsulated, reusable UI components, as seen in the `src/components/` directory structure.
    *   **Strong Ecosystem:** The project can leverage the vast ecosystem of libraries and tools available for React.
*   **Negative:**
    *   **Opinionated Configuration:** The underlying build configuration (Webpack, Babel) is abstracted away. Customizing it requires "ejecting," which is a one-way operation that increases configuration complexity.
    *   **Potential for Larger Bundle Sizes:** As an SPA framework, it ships a JavaScript bundle to the client, which can be larger than server-rendered alternatives, potentially impacting initial load time.
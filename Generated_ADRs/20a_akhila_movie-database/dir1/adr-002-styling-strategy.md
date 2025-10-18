---
### ADR-002: Styling Strategy

**Status:** Inferred
**Context:** A scalable and maintainable styling solution was needed for the component-based architecture. Global CSS stylesheets can lead to class name collisions, specificity wars, and difficulty in determining which styles affect which components. The styling needed to be tightly coupled with the component logic it applies to.
**Decision:** The project will use **`styled-components`** for a **CSS-in-JS styling approach**. This is evidenced by the `styled-components` dependency in `package.json` and the file structure pattern of having a `Component.styles.js` file alongside each component's `index.js` file (e.g., `src/components/Button/index.js` and `src/components/Button/Button.styles.js`).
**Consequences:**
*   **Positive:**
    *   **Scoped Styles:** Styles are automatically scoped to the component, eliminating the risk of global style conflicts.
    *   **Dynamic Styling:** It's easy to change styles based on component props, enabling more dynamic and responsive components.
    *   **Colocation:** Styles are located in the same directory as the component, improving developer experience and maintainability.
*   **Negative:**
    *   **Runtime Overhead:** CSS is generated and injected at runtime, which can introduce a minor performance cost compared to pre-compiled static CSS files.
    *   **Learning Curve:** Developers unfamiliar with CSS-in-JS may need time to adapt to this paradigm.
    *   **Increased Bundle Size:** The `styled-components` library adds to the final JavaScript bundle size.
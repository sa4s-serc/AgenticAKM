---
### ADR-004: Interactive Web Experience with React Components

**Status:** Inferred
**Context:** To improve the documentation's educational value, there was a need for interactive elements that would allow users to experiment with the language directly in their browser, rather than just reading static text.
**Decision:** The Astro documentation site is enhanced with interactive components built using the React library. This is evidenced by the `@astrojs/react`, `react`, and `react-dom` dependencies in `package.json`, as well as the presence of a React component file, `documentation/src/components/InteractiveRepl.jsx`.
**Consequences:**
*   **Positive:** This provides a significantly richer user experience, enabling a "show, don't just tell" approach to documentation. The interactive REPL allows users to learn and test the language without any local installation. Astro's "island architecture" allows these interactive components to be added without degrading the performance of static content.
*   **Negative:** It adds the complexity of the React framework to the documentation project's technology stack. Building and maintaining an in-browser REPL is a non-trivial task.
---
### ADR-002: Separation of Concerns via File Type

**Status:** Inferred
**Context:** A decision was needed on how to organize the frontend codebase. Code can be organized in various ways, such as by feature, by component, or by technology type. The challenge is to choose a structure that is maintainable, understandable, and promotes a clean architecture.
**Decision:** The project adopted a classic separation of concerns by file type. The structure is physically divided into three distinct files: `index.html` for content and structure, `style.css` for presentation and styling, and `index.js` for behavior and interactivity. Each file is responsible for a single, well-defined aspect of the application.
**Consequences:**
*   **Positive:**
    *   **Clarity:** This pattern is universally understood and makes it easy for developers to locate code related to structure, style, or logic.
    *   **Maintainability:** Changes to styling (in CSS) are isolated from changes to application logic (in JavaScript), reducing the risk of unintended side effects.
    *   **Efficient Caching:** Browsers can cache the CSS and JavaScript files independently. A change to the JavaScript file does not invalidate the cached CSS file, improving load times for returning visitors.
*   **Negative:**
    *   **Low Cohesion:** For component-centric UIs, the logic, markup, and styling for a single component are spread across three different files, which can increase development friction and context-switching.
    *   **Global Namespace Pollution:** Without a modularization strategy (which is not evident here), styles in `style.css` and functions/variables in `index.js` are likely global, increasing the risk of naming collisions as the project scales.
---
### ADR-003: Modular Code Architecture using ES Modules

**Status:** Inferred
**Context:** To ensure the application's source code is maintainable, scalable, and easy to reason about, a strategy for code organization was necessary. A single, monolithic JavaScript file would be unmanageable. The team needed a standardized way to define and manage dependencies between different parts of the application's logic.
**Decision:** The project uses native **JavaScript ES Modules (ESM)**. This is explicitly enabled by `"type": "module"` in `package.json` and is evident in the file structure, which breaks down the application into logical units such as `car.js`, `racetrack.js`, `fuel.js`, and a central `main.js` entry point.
**Consequences:**
*   **Positive:** This decision promotes a clean, modular architecture. Each file has a distinct responsibility, improving code readability and reusability. It enables static analysis and tree-shaking during the build process, which can lead to smaller production bundle sizes.
*   **Negative:** All code must adhere to the ESM syntax (`import`/`export`). While not a significant drawback for new projects, it requires a build tool (Vite, in this case) or a modern browser that supports it.
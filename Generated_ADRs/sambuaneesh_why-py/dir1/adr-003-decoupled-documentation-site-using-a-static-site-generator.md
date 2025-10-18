---
### ADR-003: Decoupled Documentation Site using a Static Site Generator

**Status:** Inferred
**Context:** The project requires comprehensive documentation that is user-friendly, performant, and maintainable. This documentation needs to be managed separately from the core interpreter's source code to allow for independent development and deployment.
**Decision:** A dedicated documentation website was created as a separate sub-project within the `documentation/` directory. The Astro framework, a modern static site generator, was chosen for this purpose. This is confirmed by the `astro.config.mjs` file and the dependencies in `documentation/package.json` (`astro`, `@astrojs/starlight`).
**Consequences:**
*   **Positive:** The documentation is completely decoupled from the Python interpreter, allowing for a modern web-based presentation without complicating the interpreter's codebase. Using a static site generator results in a fast, secure, and easily deployable website. Content management is simplified through Markdown files (`.md`, `.mdx`).
*   **Negative:** This introduces a second technology stack (Node.js, JavaScript/TypeScript, Astro) that must be learned and maintained. A build process is required to synchronize content, as shown by the `copy-interpreter.js` script, which adds a layer of complexity.
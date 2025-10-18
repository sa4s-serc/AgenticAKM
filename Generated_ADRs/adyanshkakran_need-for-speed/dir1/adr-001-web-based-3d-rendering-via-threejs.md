### ADR-001: Web-Based 3D Rendering via Three.js

**Status:** Inferred
**Context:** The project required the development of a real-time, interactive 3D application, specifically a car racing game. The primary architectural challenge was choosing a rendering engine that was accessible to a wide audience without requiring native installations, while still providing the necessary features for 3D graphics, model loading, and user interaction.
**Decision:** The application is built as a web application using the **Three.js** library. Three.js acts as a high-level abstraction over the browser's WebGL API, simplifying the creation and management of 3D scenes, cameras, lighting, and objects. This is confirmed by the presence of `"three": "^0.149.0"` in the `package.json` dependencies.
**Consequences:**
*   **Positive:** The application is highly accessible, running in any modern web browser without user installation. It leverages the vast JavaScript ecosystem and the skills of web developers. The library has strong community support and documentation.
*   **Negative:** Performance is inherently limited by the user's browser and hardware capabilities, and may not match that of a native desktop application. It is dependent on the browser's WebGL implementation and its potential limitations.
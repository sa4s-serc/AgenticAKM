---
### ADR-002: Adopt a Multi-Process Architecture

**Status:** Inferred
**Context:** In Electron, security and stability are paramount. Rendering untrusted remote content or even complex local UI code in the same process that has full system access is a significant security risk. A crash in the UI rendering logic could also bring down the entire application. The architectural challenge was to structure the application in a way that isolates the user interface from core application logic and system resources.
**Decision:** The application was structured using Electron's standard multi-process architecture. This is indicated by the presence of `index.js` (the "main" process entry point defined in `package.json`), `renderer.js` (logic for a "renderer" process), and `preload.js`. The preload script acts as a secure bridge, exposing specific Node.js functionalities to the renderer process without granting it full system access.
**Consequences:**
*   **Positive:**
    *   **Enhanced Security:** The renderer process, which handles the UI, runs in a sandboxed environment, mitigating risks. The `preload.js` script enforces a clear and secure boundary between the UI and the backend.
    *   **Improved Stability:** A crash or freeze in a renderer process (e.g., `renderer.js` or `leaderboard.js`) will not crash the main process, allowing the application to recover gracefully by, for example, reloading the window.
    *   **Clear Separation of Concerns:** Core application lifecycle and native OS integrations are managed in the main process, while all UI-related tasks are handled in renderer processes.
*   **Negative:**
    *   **Increased Complexity:** Developers must manage Inter-Process Communication (IPC) to send data and messages between the main and renderer processes, which adds a layer of complexity compared to a single-process application.
### ADR-001: Use Electron for Desktop Application Development

**Status:** Inferred
**Context:** The project required the creation of a desktop application, likely to provide a richer, more integrated user experience than a standard web application. The development team needed a way to build this application efficiently, potentially leveraging existing skills. The challenge was choosing a framework that could deliver a cross-platform desktop experience without the steep learning curve and development overhead of native toolkits for each operating system (e.g., C# for Windows, Swift for macOS).
**Decision:** The Electron framework was chosen to build the application. This is evident from the `electron` dependency in `package.json` and the `"start": "electron ."` script, which is the standard command to run an Electron application.
**Consequences:**
*   **Positive:**
    *   Allows developers to build a desktop application using common web technologies (HTML, CSS, JavaScript), leveraging existing skills and a vast ecosystem of web libraries.
    *   Enables the creation of a cross-platform application (Windows, macOS, Linux) from a single codebase, significantly reducing development and maintenance effort.
    *   Provides access to both browser APIs for UI rendering and Node.js APIs for powerful backend and OS-level interactions (like file system access).
*   **Negative:**
    *   Results in a larger application bundle size and higher memory consumption compared to a fully native application, as it includes a full Chromium rendering engine and a Node.js runtime.
    *   The abstraction layer can sometimes introduce performance overhead or limitations not present in native development.
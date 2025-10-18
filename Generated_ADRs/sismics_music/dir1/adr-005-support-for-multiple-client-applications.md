---
### ADR-005: Support for Multiple Client Applications

**Status:** Inferred
**Context:** The goal was to allow users to access and control their music from different devices and environments, not just a web browser. This required an architecture where the core logic was independent of any single client implementation.
**Decision:** The system was designed around an API-first principle, supporting multiple distinct client applications:
1.  **Web Client:** The primary `music-web` module, an AngularJS SPA.
2.  **Native Mobile Client:** A dedicated Android application, located in the `music-android` module and built with Gradle.
3.  **Desktop Client:** A Java-based desktop "Agent" (`music-agent`) with a graphical user interface (suggested by `AgentFrame.java`, `TrayController.java`) for local server management and control.
**Consequences:**
*   **Positive:**
    *   Provides a broad reach across web, mobile (Android), and desktop platforms.
    *   The API-centric design ensures the backend is decoupled and reusable.
*   **Negative:**
    *   Significantly increases development and maintenance effort, as code and features must be implemented and synchronized across multiple codebases (Java/Android, JavaScript/AngularJS, Java/Swing).
    *   Maintaining a consistent user experience and feature parity across all clients is a major challenge.
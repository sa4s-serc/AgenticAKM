### ADR-001: Multi-Module Monorepo for a Multi-Component System

**Status:** Inferred
**Context:** The project encompasses several distinct but related components: a shared core logic library, a web application server, a native Android client, a desktop agent, and packaging artifacts for various platforms. Managing these as separate repositories would introduce complexity in versioning, dependency management, and maintaining a consistent build process.
**Decision:** The project is structured as a multi-module monorepo managed by Apache Maven. A parent `pom.xml` in the root directory defines common dependencies and properties for sub-modules like `music-core`, `music-web`, `music-agent`, `music-android`, and various `music-distribution-*` modules.
**Consequences:**
*   **Positive:**
    *   Simplifies dependency management between internal modules (e.g., `music-web` depending on `music-core`).
    *   Ensures consistent versioning and a unified build lifecycle across the entire system.
    *   Facilitates large-scale refactoring across different components within a single commit.
*   **Negative:**
    *   The build process can become slower as the project grows.
    *   The tight coupling might make it harder for individual component teams to work and release independently.
    *   The repository contains a mix of technologies (Maven for Java, Gradle for Android, npm/Grunt for frontend), which increases cognitive load for new developers.
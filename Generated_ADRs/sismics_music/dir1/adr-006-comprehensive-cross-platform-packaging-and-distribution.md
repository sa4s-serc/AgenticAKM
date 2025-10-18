---
### ADR-006: Comprehensive Cross-Platform Packaging and Distribution

**Status:** Inferred
**Context:** To make the self-hosted server accessible to a wide range of users, it needed to be easy to install and run on all major operating systems and deployment environments, including modern containerized platforms.
**Decision:** A sophisticated, multi-pronged distribution strategy was implemented using dedicated Maven modules (`music-distribution-*`). The application is packaged into multiple formats:
*   **Standalone:** A universal, executable `.jar` file with an embedded server.
*   **OS-Native:** Installers and packages for Windows (`launch4j`, NSIS), macOS (`osxappbundle`), Debian (`.deb`), and Red Hat (`.rpm`).
*   **Containerized:** A Docker image defined by a `Dockerfile` and a `docker-compose.yml` for easy deployment.
**Consequences:**
*   **Positive:**
    *   Provides an excellent installation and deployment experience for users on almost any platform.
    *   Caters to both traditional sysadmins (OS packages) and users of modern infrastructure (Docker).
*   **Negative:**
    *   The build configuration is extremely complex, requiring specialized plugins and knowledge for each target platform (e.g., `rpm-maven-plugin`, NSIS scripting).
    *   Maintaining and testing all these different distribution methods is a significant and ongoing effort.
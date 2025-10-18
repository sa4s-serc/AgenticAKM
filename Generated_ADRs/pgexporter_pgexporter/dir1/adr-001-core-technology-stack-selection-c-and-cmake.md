### ADR-001: Core Technology Stack Selection: C and CMake

**Status:** Inferred

**Context:** The project required the development of a high-performance monitoring exporter for PostgreSQL. This type of application, which runs continuously as a daemon, must have low resource overhead (CPU and memory) to avoid impacting the performance of the database server it's monitoring. The build process must also manage numerous external libraries and support compilation on various Linux distributions.

**Decision:** The project was implemented in the **C programming language** and uses **CMake** as its build system.

**Consequences:**
*   **Positive:**
    *   **Performance:** C provides direct memory management and low-level system access, resulting in a highly efficient, low-overhead executable.
    *   **Portability:** C has a well-defined standard and compilers are available for virtually all operating systems, making the core logic highly portable.
    *   **Mature Ecosystem:** C has a vast ecosystem of libraries for networking, compression, and other low-level tasks, which the project leverages (e.g., libev, OpenSSL, zlib).
    *   **Build Management:** CMake simplifies the process of finding dependencies (`FindLibev.cmake`, `FindLibYAML.cmake`), configuring the build, and generating native build files (like Makefiles) across different environments.
*   **Negative:**
    *   **Development Complexity:** C requires manual memory management, which can be a source of bugs (e.g., memory leaks, buffer overflows) and increases development time compared to memory-safe languages.
    *   **Dependency Management:** While CMake helps, managing C dependencies is less streamlined than with modern package managers like Cargo (Rust) or Go Modules.
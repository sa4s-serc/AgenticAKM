### ADR-001: C++ with CMake for Core Compiler Implementation

**Status:** Inferred

**Context:** The project requires a language and build system suitable for developing a complex, performance-sensitive application like a compiler. The language needs to offer low-level memory control for performance optimization and building intricate data structures (like ASTs), while the build system must manage dependencies across multiple modules, handle different build configurations, and be cross-platform.

**Decision:** The core compiler logic is implemented in C++. CMake is used as the build system generator to manage the project's structure, dependencies, and compilation process. The project is structured into distinct libraries (`lib/Basic`, `lib/Lexer`, `lib/Parser`, etc.) and a driver executable (`tools/driver`), all orchestrated by `CMakeLists.txt` files.

**Consequences:**
*   **Positive:**
    *   C++ provides the necessary performance and control for compiler development.
    *   CMake offers a robust, cross-platform build solution that handles the modular nature of the codebase effectively.
    *   The separation of code into libraries (`lib/`) and executables (`tools/`) promotes modularity and reusability.
*   **Negative:**
    *   C++ has a steeper learning curve and requires manual memory management, which can be a source of bugs.
    *   CMake can have complex syntax, and managing a multi-module project requires a good understanding of its principles.
    *   Compilation times for C++ can be longer compared to other languages.
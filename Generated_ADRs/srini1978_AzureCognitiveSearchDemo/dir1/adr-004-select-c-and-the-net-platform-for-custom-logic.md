---
### ADR-004: Select C# and the .NET Platform for Custom Logic

**Status:** Inferred
**Context:** A programming language and runtime environment must be chosen to implement the custom logic for the search enrichment pipeline (the Azure Function). The choice needs to be well-supported by the chosen cloud platform (Azure) and offer a robust development experience.
**Decision:** C# and the .NET platform will be the primary technology stack for developing server-side custom logic. This is evidenced by the presence of C# source files (`.cs`) and a .NET project file (`.csproj`).
**Consequences:**
*   **Positive:**
    *   C# is a first-class language on the Azure platform, with excellent tooling, documentation, and SDK support.
    *   It is a statically-typed, mature language, which can lead to more maintainable and robust code.
    *   The .NET ecosystem is extensive, providing a rich set of libraries for various tasks.
*   **Negative:**
    *   The talent pool might be different compared to other popular backend languages like Python or Node.js.
    *   Can have a slightly higher memory footprint and slower startup time (affecting cold starts) compared to some interpreted languages.
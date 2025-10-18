### ADR-001: Use of .NET 7 for the Technology Stack

**Status:** Inferred
**Context:** The project required a foundational technology stack for development. This decision involves selecting a programming language, runtime, and framework that would meet the project's functional and non-functional requirements, such as performance and developer productivity.
**Decision:** The project was built using the .NET 7 framework and the C# programming language. This is evidenced by the presence of a Visual Studio solution file (`carbonQL.sln`), C# project files (`.csproj`), C# source code files (`.cs`), and build output directories explicitly named `net7.0`.
**Consequences:**
*   **Positive:**
    *   **Cross-Platform:** .NET 7 is cross-platform, allowing the application to be developed and run on Windows, macOS, and Linux.
    *   **Performance:** .NET 7 offers significant performance improvements over its predecessors.
    *   **Unified Platform:** It provides a unified framework for building various types of applications (console, web, etc.).
    *   **Rich Ecosystem:** Access to the extensive NuGet package library for third-party dependencies.
*   **Negative:**
    *   Locks the project into the .NET ecosystem, potentially requiring specific developer skills and tooling.
    *   Future upgrades to new .NET versions will be necessary to stay on a supported framework.
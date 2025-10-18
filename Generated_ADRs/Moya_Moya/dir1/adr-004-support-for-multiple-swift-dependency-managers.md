---
### ADR-004: Support for Multiple Swift Dependency Managers

**Status:** Inferred

**Context:** The Swift community uses several different tools for managing project dependencies, primarily CocoaPods, Carthage, and the official Swift Package Manager (SPM). To be a viable choice for the widest possible range of projects, a library must be easily integrated using these popular tools. Failing to support a major dependency manager can be a significant barrier to adoption.

**Decision:** The project is configured to support all three major dependency managers. This is evidenced by the presence of:
1.  `Moya.podspec`: The specification file for integration with CocoaPods.
2.  `Cartfile`: The file used to declare dependencies for Carthage.
3.  `Package.swift`: The manifest file that enables support for Swift Package Manager.

**Consequences:**
*   **Positive:**
    *   **Maximized Reach and Adoption:** Developers can use their preferred dependency management tool, making it frictionless to add the library to their projects.
    *   **Flexibility:** The library can be used in a wide variety of project setups, from legacy projects using CocoaPods to modern ones relying solely on SPM.
*   **Negative:**
    *   **Configuration Complexity:** Maintaining configuration files for three different systems adds overhead. Each system has its own quirks and requirements.
    *   **Release Process Overhead:** The release process is more complex, as it requires updating and validating the configurations for CocoaPods, Carthage, and SPM to ensure they all work correctly.
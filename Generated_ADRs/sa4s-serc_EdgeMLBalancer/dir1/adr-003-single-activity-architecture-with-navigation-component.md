---
### ADR-003: Single-Activity Architecture with Navigation Component

**Status:** Inferred
**Context:** The application requires a structured user flow between different screens, such as a permissions check screen, a home screen, and the main camera/detection screen. A robust and maintainable navigation pattern is needed to manage this flow.
**Decision:** A Single-Activity Architecture was adopted, using Fragments to represent individual screens and the Android Jetpack Navigation Component to manage the navigation graph. Evidence includes `MainActivity.kt` as the single entry point, multiple Fragment files (`PermissionsFragment.kt`, `HomeFragment.kt`, `CameraFragment.kt`), the `navigation/nav_graph.xml` resource file, and the `navigation-safe-args-gradle-plugin` dependency for type-safe data passing between fragments.
**Consequences:**
*   **Positive:**
    *   Adheres to modern, Google-recommended Android app architecture.
    *   Simplifies UI lifecycle management compared to a multi-activity architecture.
    *   The Navigation Component provides a centralized, visual way to define and manage all app navigation paths.
    *   Safe-Args plugin provides compile-time safety when passing data between screens, reducing runtime errors.
*   **Negative:**
    *   Can introduce complexity if deep-linking or complex inter-fragment communication is not managed carefully.
*   **Trade-offs:** Chose a modern, cohesive UI architecture that simplifies development at the cost of a slight learning curve for the Navigation Component framework.
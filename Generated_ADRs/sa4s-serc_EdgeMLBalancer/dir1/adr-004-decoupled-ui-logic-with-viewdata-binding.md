---
### ADR-004: Decoupled UI Logic with View/Data Binding

**Status:** Inferred
**Context:** To connect the UI layout (XML files) with the application logic (Kotlin Fragments), a mechanism is needed that is both safe and efficient, avoiding error-prone manual view lookups with `findViewById()`.
**Decision:** The project uses Android's View Binding and Data Binding frameworks. This is confirmed by the `buildFeatures { viewBinding true }` and `dataBinding { enabled = true }` blocks in the `app/build.gradle` file, as well as the presence of generated binding classes like `FragmentCameraBinding.java` in the build directory.
**Consequences:**
*   **Positive:**
    *   Eliminates the need for `findViewById()`, reducing boilerplate code.
    *   Provides compile-time safety. If a view ID is incorrect or the layout changes, the code will fail to compile rather than crash at runtime.
    *   Improves code readability by creating a direct, type-safe reference to each view.
*   **Negative:**
    *   Adds a code generation step to the build process, which can slightly increase build times.
*   **Trade-offs:** A minor increase in build complexity is accepted in exchange for significantly improved code safety, maintainability, and developer productivity when working with UI elements.
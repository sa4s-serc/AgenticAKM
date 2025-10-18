### ADR-001: Native Android Platform with Kotlin

**Status:** Inferred
**Context:** The project required a mobile application capable of real-time camera feed processing and machine learning inference. This necessitates high performance, direct access to device hardware (like the camera), and a responsive user interface.
**Decision:** The application was developed as a native Android application using the Kotlin programming language. This is evidenced by the presence of an `app-debug.apk`, Android-specific Gradle configuration files (`build.gradle`, `AndroidManifest.xml`), and source code files with the `.kt` extension (e.g., `CameraFragment.kt`, `MainActivity.kt`). The `build.gradle` file explicitly applies the `kotlin-android` plugin.
**Consequences:**
*   **Positive:**
    *   Optimal performance and responsiveness by leveraging the native Android SDK.
    *   Full access to device hardware and platform-specific APIs.
    *   Kotlin provides modern language features like null safety, conciseness, and interoperability with Java, leading to more robust and maintainable code.
*   **Negative:**
    *   The codebase is not portable to other mobile operating systems like iOS. A separate application would need to be developed for that platform.
*   **Trade-offs:** Platform-specific performance and features were prioritized over cross-platform portability.
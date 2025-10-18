---
### ADR-002: Kotlin-first codebase with Java 8 target, using both Data Binding and View Binding

Status: Inferred
Context: Gradle config sets kotlin-android and kotlin-kapt plugins, kotlin_version 1.5.21 with jvmTarget Java 8; dataBinding { enabled = true } and buildFeatures { viewBinding true } are both enabled. Numerous generated DataBinding and ViewBinding artifacts exist.
Decision: Use Kotlin as the primary language, target Java 8 features, and enable both Data Binding and View Binding for UI development.
Consequences:
- Positive: Kotlin language features, concise UI code, type-safe view access, and reactive data-binding patterns.
- Negative: Longer build times and more generated code; mixed binding styles can add team complexity if not consistently applied.
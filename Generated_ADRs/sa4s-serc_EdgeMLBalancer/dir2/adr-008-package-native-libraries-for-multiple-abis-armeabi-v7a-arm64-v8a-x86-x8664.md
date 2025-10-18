---
### ADR-008: Package native libraries for multiple ABIs (armeabi-v7a, arm64-v8a, x86, x86_64)

Status: Inferred
Context: Build intermediates include native libs for all major ABIs for TFLite GPU and task libraries.
Decision: Ship binaries for multiple ABIs to maximize device coverage.
Consequences:
- Positive: Broad compatibility across a wide range of Android devices and emulators.
- Negative: Increases APK size; build and test matrix becomes larger.
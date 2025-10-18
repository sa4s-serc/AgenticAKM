---
### ADR-009: Release build with minification disabled

Status: Inferred
Context: buildTypes.release { minifyEnabled false } in app/build.gradle.
Decision: Disable code shrinking/obfuscation for release builds.
Consequences:
- Positive: Simplifies debugging and crash analysis; avoids potential TFLite/native reflection issues.
- Negative: Larger APK size; misses optimizations from R8/ProGuard.
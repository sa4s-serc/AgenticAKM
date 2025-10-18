---
### ADR-013: Platform targeting: minSdk 21, target/compile SDK 32, AGP 7.1.2, Kotlin 1.5.21

Status: Inferred
Context: Gradle config sets minSdkVersion 21, compile/target 32, Android Gradle Plugin 7.1.2, Kotlin 1.5.21 and Java 8.
Decision: Balance backward compatibility (API 21+) with access to modern APIs/tooling by targeting SDK 32 and current build tools for the project’s timeframe.
Consequences:
- Positive: Wide device reach while benefiting from newer platform behaviors; stable toolchain for CI and contributors.
- Negative: Some newer platform features remain unavailable; future SDK updates will require migration work.
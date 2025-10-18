---
### ADR-010: Type-safe navigation using Safe Args

Status: Inferred
Context: Plugin "androidx.navigation.safeargs.kotlin" is applied; generated Directions classes are present.
Decision: Use Navigation Safe Args to pass arguments between Fragments in a type-safe manner.
Consequences:
- Positive: Compile-time safety for navigation arguments; clearer contracts between screens.
- Negative: Additional Gradle processing and generated code; navigation graph changes require rebuilds.
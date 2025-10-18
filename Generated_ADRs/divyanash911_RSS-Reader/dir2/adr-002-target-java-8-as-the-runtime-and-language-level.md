---
### ADR-002: Target Java 8 as the runtime and language level

Status: Inferred
Context: The POM sets maven.compiler.source and maven.compiler.target to 1.8. This constrains the language features and bytecode compatibility for the project.
Decision: Standardize on Java 8 for both compilation and runtime compatibility.
Consequences:
- Positive: Stable, widely supported baseline at the time; broad ecosystem compatibility.
- Negative: Cannot use features from newer Java versions; may necessitate older library versions for compatibility.
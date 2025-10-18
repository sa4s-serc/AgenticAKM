### ADR-001: Centralized build and dependency management with a Maven parent POM

Status: Inferred
Context: The repository defines a parent POM (artifactId: reader-parent, packaging: pom) with many dependency versions declared as properties. This indicates a need to coordinate versions and configuration across multiple modules and ensure reproducible builds.
Decision: Use Apache Maven with a parent POM to centralize dependency versions, compiler configuration, and shared build settings for all modules.
Consequences: 
- Positive: Consistent dependency versions across modules, easier upgrades, reproducible builds, simpler module onboarding.
- Negative: Coupled to Maven’s lifecycle; managing pinned versions can lead to lag behind newer releases.
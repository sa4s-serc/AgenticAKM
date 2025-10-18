---
### ADR-009: Use Maven as the build system with Lombok and Spring Boot plugins

Status: Inferred
Context: The project requires a conventional Java build tool with dependency management and support for annotation processing.
Decision: Use Maven with Spring Boot parent POM; include Lombok to reduce boilerplate; configure annotationProcessorPaths in the maven-compiler-plugin; include spring-boot-starter-test for testing.
Consequences:
- Positive: Standardized builds, dependency management, reduced boilerplate with Lombok, easy test setup.
- Negative: Lombok requires IDE configuration and can complicate tooling; Maven adds XML configuration overhead.
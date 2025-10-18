### ADR-001: Adopt Spring Boot 3.5 with Java 21 for the backend

Status: Inferred
Context: The project requires a modern, production-ready framework for building a RESTful backend with minimal boilerplate and strong ecosystem support.
Decision: Use Spring Boot 3.5.0 with Java 21 (as specified in pom.xml) as the application framework and runtime.
Consequences: 
- Positive: Rapid development, auto-configuration, rich ecosystem, long-term support, modern Java language features.
- Negative: Requires Java 21 runtime; all dependencies must be compatible with Spring Boot 3.x and Jakarta namespace changes.
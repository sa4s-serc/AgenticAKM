---
### ADR-005: Organize source by domain-focused ES modules

Status: Inferred
Context: The src directory contains car.js, fuel.js, cartrack.js, racetrack.js, and main.js, indicating a separation by domain/feature rather than monolithic code.
Decision: Use small, domain-oriented ES modules to encapsulate game elements and scene setup.
Consequences:
- Positive: Improves readability, testability (unit-level), and maintainability; enables clear ownership of responsibilities.
- Negative: Requires careful management of shared state and inter-module dependencies; potential coupling around Three.js scene and lifecycle management.
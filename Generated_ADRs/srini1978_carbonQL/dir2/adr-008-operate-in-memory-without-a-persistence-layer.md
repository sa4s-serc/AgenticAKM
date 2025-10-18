---
### ADR-008: Operate in-memory without a persistence layer

Status: Inferred
Context: There are no database-related files, configuration, or persistence libraries; only models and calculation logic are visible.
Decision: Keep the application stateless/in-memory, focusing on calculation and transformation without persistence.
Consequences:
- Positive: Simpler architecture, fewer components to manage, easier local execution and testing.
- Negative: No durability, replay, or historical tracking; scaling to stateful scenarios will require additional design and components.
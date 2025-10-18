---
### ADR-006: Use Plain Old CLR Objects (POCOs) for domain models

Status: Inferred
Context: The presence of Model/EtsyModels.cs suggests simple, typed classes for representing domain data without external frameworks.
Decision: Represent domain data with POCOs to keep models simple and framework-agnostic.
Consequences:
- Positive: Easy to serialize, test, and evolve; minimal dependencies.
- Negative: Requires manual enforcement of invariants/validation; lacks built-in features offered by richer ORM or validation frameworks.
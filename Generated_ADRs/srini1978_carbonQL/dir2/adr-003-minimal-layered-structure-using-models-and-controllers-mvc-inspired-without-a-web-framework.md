---
### ADR-003: Minimal layered structure using Models and Controllers (MVC-inspired without a web framework)

Status: Inferred
Context: The backend library organizes code into Controller/EtsyCalculations.cs and Model/EtsyModels.cs, suggesting an MVC-inspired separation, but there is no web framework present.
Decision: Use simple folder and class layering (Model for data contracts, Controller for orchestration/calculation) within a class library, without introducing a full web/MVC framework.
Consequences:
- Positive: Lightweight structure, clear separation between data representation and processing logic, easy to evolve.
- Negative: “Controller” naming outside a web context may be confusing; lacks framework-provided features (routing, filters) if/when moving to a web host.
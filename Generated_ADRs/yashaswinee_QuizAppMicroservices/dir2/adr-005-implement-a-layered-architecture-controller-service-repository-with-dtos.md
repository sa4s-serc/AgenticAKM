---
### ADR-005: Implement a layered architecture (Controller → Service → Repository) with DTOs

Status: Inferred
Context: Maintain separation of concerns between API, business logic, and persistence; avoid exposing entities directly over the wire.
Decision: 
- Controllers: QuestionController, QuizController for REST endpoints.
- Services: QuestionService, QuizService encapsulate business logic.
- Repositories/DAOs: QuestionDao, QuizDao manage persistence.
- DTOs: QuestionWrapper, QuizResponse decouple API contracts from entities.
Consequences:
- Positive: Clear boundaries, testability of business logic, flexibility to evolve API and domain independently, better security by not exposing entities.
- Negative: Additional mapping between entities and DTOs; more classes to maintain.
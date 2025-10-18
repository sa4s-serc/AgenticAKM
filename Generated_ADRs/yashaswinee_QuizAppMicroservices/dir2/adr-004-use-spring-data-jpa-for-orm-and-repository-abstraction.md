---
### ADR-004: Use Spring Data JPA for ORM and repository abstraction

Status: Inferred
Context: The application needs to persist domain entities and perform CRUD and query operations with minimal boilerplate.
Decision: Use Spring Data JPA (spring-boot-starter-data-jpa) with repository interfaces (QuestionDao, QuizDao) to abstract data access.
Consequences:
- Positive: Rapid development, reduced boilerplate, easy pagination/sorting, derived queries, integration with transaction management.
- Negative: Performance tuning and complex queries may require custom JPQL/SQL; abstraction can obscure generated SQL; careful entity mapping needed.
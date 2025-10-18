---
### ADR-010: Run the application on the host and the database in a container

Status: Inferred
Context: Simplify developer workflow and reduce container orchestration complexity while still isolating the database.
Decision: Only the database is containerized via docker-compose; the Spring Boot app runs natively on the host, connecting to the Postgres container.
Consequences:
- Positive: Faster edit–run cycle for the app; avoids building and managing an application container during development.
- Negative: Potential environment differences if production uses containers for the app; requires correct networking/config to connect host app to container DB.
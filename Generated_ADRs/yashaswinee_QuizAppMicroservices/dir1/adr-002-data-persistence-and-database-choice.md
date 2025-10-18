---
### ADR-002: Data Persistence and Database Choice

**Status:** Inferred

**Context:** The application needs a reliable way to store, manage, and retrieve relational data, specifically for quizzes and questions. An architectural choice was required for both the database technology and the method of interaction from the Java application code.

**Decision:** A **PostgreSQL** relational database is used for data storage. The application interacts with the database via **Spring Data JPA** (Java Persistence API), with Hibernate as the underlying ORM provider. This is inferred from the `pom.xml` dependencies (`spring-boot-starter-data-jpa`, `postgresql`) and the `docker-compose.yml` file, which defines a `postgres:15` service.

**Consequences:**
*   **Positive:**
    *   JPA/ORM abstracts away most of the boilerplate SQL, allowing developers to work with Java objects and improving productivity.
    *   The use of a powerful, open-source RDBMS like PostgreSQL provides advanced features, reliability, and strong data integrity.
    *   Spring Data JPA further simplifies the data access layer by providing repository interfaces out-of-the-box.
*   **Negative:**
    *   ORM can introduce a layer of complexity and may generate inefficient SQL queries if not used carefully, potentially leading to performance issues (e.g., N+1 problem).
    *   Developers need to be familiar with JPA concepts like entity lifecycles, transaction management, and fetching strategies.
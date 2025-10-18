---
### ADR-003: Relational Database with JDBI for Data Persistence

**Status:** Inferred
**Context:** The application needs to persistently store and manage structured data for users, music metadata (artists, albums, tracks), playlists, and configurations. A reliable and queryable data storage solution was essential.
**Decision:** A relational database is used as the persistence layer. The interaction with the database is handled by the JDBI library, rather than a full-fledged ORM like Hibernate. This is evidenced by the `org.jdbi.jdbi` dependency and the presence of numerous Data Access Object (DAO) classes (e.g., `AlbumDao.java`, `TrackDao.java`) and `Mapper` classes in the `music-core` module. Database connection pooling is managed by C3P0.
**Consequences:**
*   **Positive:**
    *   JDBI offers direct control over SQL, allowing for fine-tuned and optimized database queries.
    *   It's a lightweight library with less "magic" than a full ORM, which can make debugging and performance tuning more straightforward.
    *   The DAO pattern provides a clear separation between business logic and data access logic.
*   **Negative:**
    *   Requires writing and maintaining more SQL manually compared to an ORM, which can be more labor-intensive.
    *   The presence of SQL update scripts (`db/update/dbupdate-*.sql`) suggests a manual or simple database migration strategy, which might be error-prone.
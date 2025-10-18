---
### ADR-002: Use relational storage with JDBI and handwritten SQL, pooled by c3p0

Status: Inferred
Context: music-core uses org.jdbi (v2.x) with DAOs, mappers, criteria objects, and versioned SQL scripts under src/main/resources/db/update. Connection pooling is via c3p0. Tests use H2 and c3p0 properties.
Decision: Implement persistence with JDBI (SQL object/handle APIs), custom mappers/DTOs, and explicit SQL migration scripts; manage connections using c3p0.
Consequences:
- Positive: Fine-grained control over SQL; lightweight compared to full ORM; easy to profile and optimize queries; portability across RDBMS; straightforward testing with H2.
- Negative: More boilerplate (mappers/DTOs); manual schema evolution responsibility; fewer high-level ORM conveniences (cascades, lazy loading).
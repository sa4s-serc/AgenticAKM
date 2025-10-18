# ADR-010: No explicit DB/ORM packages declared

**Date**: 2025-10-14
**Status**: Proposed

## Context
requirements.txt contains no obvious database drivers or ORMs (e.g., SQLAlchemy, psycopg, pymongo).

## Decision
Avoid commit to a specific external database client/ORM at this stage.

## Consequences
- Lower initial complexity and smaller dependency footprint
- If persistence is required, likely relies on Python’s stdlib (e.g., sqlite3) or an external service via HTTP
- Missing migration/versioning tooling; future adoption will require schema and data lifecycle planning
- Easier to swap in a datastore later but with potential refactoring cost
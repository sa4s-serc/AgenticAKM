---
### ADR-008: Provide full-text search via Apache Lucene

Status: Inferred
Context: music-core declares an Apache Lucene dependency; indexing/reindex async events exist; search REST resource is present (SearchResource).
Decision: Use Lucene to index and query music metadata for fast search capabilities.
Consequences:
- Positive: Fast, flexible text search; ranking and query features; local index avoids DB LIKE performance issues.
- Negative: Index synchronization complexity; storage overhead; reindexing strategy required for large libraries.
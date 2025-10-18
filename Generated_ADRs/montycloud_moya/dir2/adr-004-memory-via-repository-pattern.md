---
### ADR-004: Memory via Repository Pattern

Status: Inferred
Context: The framework needs flexible storage for conversation histories and other state, supporting both ephemeral and persistent use cases without forcing a specific database.
Decision: Define a memory Repository interface (moya/memory/repository.py) with InMemoryRepository and FileSystemRepo implementations.
Consequences:
- Positive: Swappable backends; easy local development and testing; no external dependencies required for basic persistence.
- Negative: File system storage may not scale or support concurrency; production deployments may need additional backends (DB, cloud stores) not yet provided.
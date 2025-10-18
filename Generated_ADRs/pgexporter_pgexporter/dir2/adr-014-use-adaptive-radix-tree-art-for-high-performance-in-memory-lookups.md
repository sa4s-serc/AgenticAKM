---
### ADR-014: Use Adaptive Radix Tree (ART) for high-performance in-memory lookups

Status: Inferred
Context: art.c and art.h are included, indicating usage of ART as a core data structure for key-value lookups (e.g., metrics registry or configuration indexes).
Decision: Employ an Adaptive Radix Tree for fast, memory-efficient string key lookups.
Consequences:
- Positive: High performance for prefix-based and exact lookups; good memory locality.
- Negative: More complex than simple hash maps; specialized maintenance and testing.
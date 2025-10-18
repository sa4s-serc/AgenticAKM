---
### ADR-010: Utility libraries for common tasks (Apache Commons and Guava)

Status: Inferred
Context: Dependencies include commons-lang 2.6, commons-io 2.1, commons-compress 1.18, and Guava 14.0.
Decision: Use mature utility libraries to avoid reinventing common functionality.
Consequences:
- Positive: Faster development, fewer bugs for common tasks, well-tested utilities.
- Negative: Version lag and possible overlap between libraries; risk of shaded or transitive conflicts; Guava’s older version lacks newer APIs and bug fixes.
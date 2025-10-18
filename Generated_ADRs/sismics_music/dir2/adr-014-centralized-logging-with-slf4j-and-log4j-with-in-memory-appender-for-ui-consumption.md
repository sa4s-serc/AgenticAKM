---
### ADR-014: Centralized logging with SLF4J and Log4j, with in-memory appender for UI consumption

Status: Inferred
Context: Dependencies include slf4j-api, slf4j-log4j12, log4j; music-core contains a MemoryAppender and log utilities; web UI exposes logs in settings.
Decision: Use SLF4J as the logging façade with Log4j backend; provide an in-memory appender to surface logs in the administration UI.
Consequences:
- Positive: Uniform logging API; easy integration into UI for diagnostics; flexible configuration per environment.
- Negative: Log4j 1.x is end-of-life and poses security/maintenance risks; memory appender must be bounded to avoid leaks.
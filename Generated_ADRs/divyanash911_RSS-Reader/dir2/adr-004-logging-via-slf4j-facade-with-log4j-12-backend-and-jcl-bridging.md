---
### ADR-004: Logging via SLF4J facade with Log4j 1.2 backend and JCL bridging

Status: Inferred
Context: Dependencies include slf4j (1.6.x), log4j 1.2.16, and jcl-over-slf4j, suggesting SLF4J as the facade, Log4j as the backend, and bridging of Apache Commons Logging.
Decision: Standardize application logging on SLF4J, bridge Commons Logging to SLF4J, and use Log4j 1.2 as the logging backend.
Consequences:
- Positive: Unified logging API across the codebase and third-party libs; flexibility to swap backends later.
- Negative: Log4j 1.2 is end-of-life and has known security risks; careful exclusion/bridging management required.
---
### ADR-014: Favor stability/compatibility over latest library versions

Status: Inferred
Context: Many dependencies are pinned to relatively old versions (e.g., Guava 14.0, JUnit 4.7, SLF4J 1.6.x, PostgreSQL 9.4 JDBC jre7), even while using Java 8.
Decision: Prefer proven, stable versions of dependencies to maintain compatibility and reduce upgrade risk.
Consequences:
- Positive: Predictable behavior; fewer breaking changes; easier maintenance for long-lived deployments.
- Negative: Missed performance, security, and feature improvements; potential exposure to known vulnerabilities in legacy versions; eventual larger upgrade effort.
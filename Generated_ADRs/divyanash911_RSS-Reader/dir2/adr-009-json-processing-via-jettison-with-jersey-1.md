---
### ADR-009: JSON processing via Jettison with Jersey 1

Status: Inferred
Context: org.codehaus.jettison:jettison 1.1 is included and commonly used with Jersey 1 for JSON processing (JAXB/JSON mapping).
Decision: Use Jettison as the JSON provider for Jersey 1.
Consequences:
- Positive: Straightforward integration with Jersey 1’s ecosystem.
- Negative: Performance and feature limitations compared to modern JSON libraries (e.g., Jackson); migration advisable when upgrading the REST stack.
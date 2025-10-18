---
### ADR-011: Email testing and SMTP simulation with SubEthaSMTP and Wiser

Status: Inferred
Context: Dependencies for SubEthaSMTP (3.1.6) and Wiser (1.2) indicate simulated SMTP used in tests.
Decision: Use SubEthaSMTP/Wiser to simulate SMTP servers for testing email-related features.
Consequences:
- Positive: Deterministic email tests without external dependencies; faster CI runs.
- Negative: Differences between simulated and real SMTP servers may hide production-specific issues.
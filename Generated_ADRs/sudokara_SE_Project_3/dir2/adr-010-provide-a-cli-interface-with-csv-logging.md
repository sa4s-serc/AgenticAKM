---
### ADR-010: Provide a CLI interface with CSV logging

**Status:** Inferred
**Context:** src/phoenix/CLI/cli.py exists; logs are stored as log and log.csv; no GUI or web server present.
**Decision:** Expose functionality via a command-line interface and record operational telemetry in CSV for simplicity and portability.
**Consequences:** 
- Positive: Low overhead; scriptable; easy integration with cron/systemd; CSV is widely consumable (e.g., by pandas).
- Negative: Limited user-friendliness; less suitable for real-time dashboards; parsing logs for complex analytics may be cumbersome.
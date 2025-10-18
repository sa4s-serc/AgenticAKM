---
### ADR-007: Instrument per-phase energy and system metrics, logging MAPE-K overhead

Status: Inferred
Context: MAPEK_energy.csv exists in EcoMLS and results directories; log.csv and monitor.csv are captured per episode and per approach.
Decision: Track and log energy consumption and related metrics per MAPE-K phase and overall execution to assess adaptation overhead.
Consequences:
- Positive: Enables fine-grained attribution of costs; supports tuning and optimization; improves observability.
- Negative: Adds logging overhead; requires careful synchronization of metrics across phases.
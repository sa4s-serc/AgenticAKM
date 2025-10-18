---
### ADR-011: Validate algorithms across both trading and benchmark control tasks

Status: Inferred
Context: Presence of SAC checkpoints for Hopper-v4 (models/SAC_Hopper-v4__SAC__... .pth) alongside trading-focused artifacts and plots.
Decision: Use standard benchmark environments (e.g., Hopper-v4) in addition to trading tasks to validate algorithm correctness and generality.
Consequences:
- Positive: Increases confidence in implementations by cross-verifying on known benchmarks; helps isolate environment-specific vs. algorithmic issues.
- Negative: Adds dependency on benchmark environment setup; splits experimentation time between domains.
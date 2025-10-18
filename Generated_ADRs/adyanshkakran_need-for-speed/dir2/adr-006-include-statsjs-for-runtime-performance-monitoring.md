---
### ADR-006: Include Stats.js for runtime performance monitoring

Status: Inferred
Context: stats.js@^0.17.0 is a dependency, commonly used to monitor FPS and frame timings during development.
Decision: Integrate Stats.js to observe performance during runtime.
Consequences:
- Positive: Quick feedback on performance hotspots and regressions; useful for tuning assets and code paths.
- Negative: Minor runtime overhead; should be disabled or excluded in production builds to avoid unnecessary costs.
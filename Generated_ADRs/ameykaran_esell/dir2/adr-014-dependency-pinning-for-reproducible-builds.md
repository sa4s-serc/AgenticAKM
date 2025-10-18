---
### ADR-014: Dependency pinning for reproducible builds

Status: Inferred
Context: requirements.txt pins many packages to exact versions (including heavy multimedia libs); frontend uses exact Next/React versions.
Decision: Pin backend and frontend dependencies tightly to specific versions for reproducibility.
Consequences:
- Positive: Stable builds; fewer surprises across environments.
- Negative: Security updates require regular curation; potential version conflicts and upgrade friction.
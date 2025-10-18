---
### ADR-004: Local filesystem as primary storage for inputs and generated artifacts

Status: Inferred
Context: backend/uploads and backend/posters contain per-user artifacts; backend/video/final_output and prompts/templates are file-based; no DB or cloud storage dependencies present.
Decision: Store user uploads and generated outputs (HTML posters, videos, audio) on the server filesystem.
Consequences:
- Positive: Simple, fast, no external services; easy developer onboarding.
- Negative: Not horizontally scalable; persistence and backup are manual; multi-instance deployments require shared storage or refactor.
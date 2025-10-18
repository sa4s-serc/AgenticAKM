---
### ADR-015: CLI-friendly orchestration for video pipeline

Status: Inferred
Context: backend/video/run.py and run.sh exist alongside the API; prompts/configs are file-based.
Decision: Keep the video pipeline runnable via scripts in addition to API calls, enabling local batch runs and debugging.
Consequences:
- Positive: Developer-friendly; supports offline experimentation and CI jobs.
- Negative: Potential duplication between script and API orchestration; must keep interfaces in sync.
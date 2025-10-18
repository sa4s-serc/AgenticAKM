---
### ADR-015: Logging, Usage Tracking, and Observability Hooks

Status: Inferred
Context: Users need to debug, monitor, and optionally track usage for optimization and troubleshooting.
Decision: Provide logging utilities and toggles (utils/logging_utils.py, utils/enable_litellm_logging.py, disable variants), a usage tracker (utils/usage_tracker.py), and inspection helpers (utils/inspect_history.py).
Consequences:
- Positive: Better debuggability and telemetry; optional integrations with external routers (LiteLLM).
- Negative: Privacy and compliance considerations; configuration complexity; risk of noisy logs.
---
### ADR-005: Use TensorBoard event logging for experiment tracking

Status: Inferred
Context: Numerous TensorBoard event files under logs/ with timestamped run directories and train subdirectories indicate run-based metrics tracking.
Decision: Standardize on TensorBoard for logging training and evaluation metrics across algorithms and runs.
Consequences:
- Positive: Unified visualization and comparison across experiments; compatibility with common tooling; supports long-running training diagnostics.
- Negative: Requires disciplined run management and storage; event-file proliferation can increase disk usage and archiving needs.
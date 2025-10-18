---
### ADR-004: Use MAPE as the primary performance metric and trigger

Status: Inferred
Context: The project structure (mape/ folder), files like mape_info.json and mape_log.csv, and thresholds.json indicate Mean Absolute Percentage Error is the central KPI for monitoring and planning actions.
Decision: Use MAPE as the main accuracy/performance signal for monitoring, alerting, and drift/retraining decisions, with thresholds defined in thresholds.json.
Consequences:
- Positive: Intuitive, scale-free metric; facilitates thresholding across series/scales.
- Negative: Undefined or unstable when true values approach zero; can overweight small denominators; may not capture all facets of model performance.
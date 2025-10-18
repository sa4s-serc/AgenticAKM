---
### ADR-006: Externalize approach/strategy selection via configuration

Status: Inferred
Context: approach.conf and set_approach.sh suggest the ability to switch strategies/approaches without code changes (e.g., different monitoring or retraining strategies).
Decision: Manage operational approach selection via an external configuration file and helper shell script.
Consequences:
- Positive: Easier experimentation and A/B of strategies; reduces code churn; supports automation.
- Negative: Configuration drift risk; shell script reliance can be environment-dependent.
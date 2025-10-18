---
### ADR-002: Standardize on Gymnasium and gym-trading-env for environment interfaces

Status: Inferred
Context: Requirements specify gymnasium==0.29.1 and gym-trading-env==0.3.3. The codebase includes env.py and runs both trading tasks and classic control (e.g., Hopper-v4 in SAC models).
Decision: Use Gymnasium as the unified RL API and gym-trading-env for market simulation to ensure consistent interfaces across trading and benchmark environments.
Consequences:
- Positive: Consistent environment APIs across tasks; easier swapping between trading and benchmark environments (e.g., Hopper-v4).
- Negative: Tied to Gymnasium’s versioning and API changes; dependency on third-party trading environment capabilities and limitations.
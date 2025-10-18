---
### ADR-003: Implement algorithms in-house rather than relying on high-level RL libraries

Status: Inferred
Context: The repo includes standalone implementations for DQN, DDPG, SAC, and VPG without dependencies like Stable-Baselines3. Custom training loops and logging are present.
Decision: Build and maintain custom RL implementations for core algorithms instead of adopting an external RL framework.
Consequences:
- Positive: Full control over algorithm behavior, customization, and research flexibility; easier to inspect and modify training details.
- Negative: Reinventing components (buffers, networks, schedulers) increases complexity and risk of subtle bugs; more effort to ensure correctness and performance.
---
### ADR-004: Support both discrete and continuous action spaces

Status: Inferred
Context: Presence of DQN (discrete), DDPG/SAC (continuous), and separate scripts VPG-discrete.py and VPG-continuous.py, plus trading data and plots per asset.
Decision: Architect the system to handle both discrete and continuous action spaces, with algorithm choices aligned accordingly (e.g., DQN for discrete, DDPG/SAC/VPG for continuous).
Consequences:
- Positive: Broader applicability of the platform to different market formulations and strategies; enables algorithm-to-action-space alignment.
- Negative: Duplicated logic and branching across code paths; more testing burden and increased configuration surface.
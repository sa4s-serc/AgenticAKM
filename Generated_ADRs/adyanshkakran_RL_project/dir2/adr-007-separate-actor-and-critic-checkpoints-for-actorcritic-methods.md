---
### ADR-007: Separate actor and critic checkpoints for actor–critic methods

Status: Inferred
Context: Dedicated files actor_DDPG.pth and critic_DDPG.pth, along with models/actor_DDPG.pth and models/critic_DDPG.pth, indicate separate persistence.
Decision: Save actor and critic networks independently for actor–critic algorithms (e.g., DDPG).
Consequences:
- Positive: Enables selective restoration, transfer learning, and independent evaluation; can simplify debugging and ablations.
- Negative: Requires careful synchronization and bookkeeping; more files and potential mismatch risks during load.
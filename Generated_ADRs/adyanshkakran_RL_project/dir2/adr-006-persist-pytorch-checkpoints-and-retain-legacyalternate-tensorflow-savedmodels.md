---
### ADR-006: Persist PyTorch checkpoints and retain legacy/alternate TensorFlow SavedModels

Status: Inferred
Context: Model artifacts include .pth files (e.g., models/SAC_Hopper-v4__... .pth, actor_DDPG.pth, critic_DDPG.pth) and TensorFlow SavedModel directories (e.g., models/2x256___... .model/, models/DQN_KO_PEP__... .model/).
Decision: Save current models primarily as PyTorch .pth files while keeping TensorFlow SavedModel artifacts from related experiments for reference or comparability.
Consequences:
- Positive: Flexibility to leverage current PyTorch workflows while preserving historical or alternative TF models; supports cross-framework analysis.
- Negative: Mixed framework artifacts complicate environment setup and dependency management; risk of confusion over which artifacts are canonical.
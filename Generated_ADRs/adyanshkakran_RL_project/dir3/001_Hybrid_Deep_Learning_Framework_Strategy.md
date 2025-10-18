# ADR-001: Hybrid Deep Learning Framework Strategy

**Date**: 2025-10-14
**Status**: Proposed

## Context
The project's goal was to implement and compare a diverse set of Reinforcement Learning algorithms, from foundational ones like DQN to state-of-the-art methods like DDPG and SAC. Reference implementations and tutorials for these algorithms are readily available across different deep learning frameworks.

## Decision
To use two different deep learning frameworks concurrently: TensorFlow/Keras was chosen for the Deep Q-Network (DQN) agent, while PyTorch was used for the more complex Deep Deterministic Policy Gradient (DDPG), Soft Actor-Critic (SAC), and Vanilla Policy Gradient (VPG) agents.

## Consequences
This multi-framework approach likely accelerated initial development by allowing the reuse of existing, framework-specific algorithm implementations. However, it introduced significant technical debt by increasing dependency complexity, creating an inconsistent codebase, and complicating the environment setup for new contributors. It makes code standardization and maintenance more challenging.
# ADR-004: Implementation of a Diverse Range of RL Algorithms

**Date**: 2025-10-14
**Status**: Proposed

## Context
To solve the complex problem of portfolio allocation, it was necessary to determine which class of RL algorithms would be most effective. The action space (portfolio weights) is continuous, but simpler discrete actions (buy/sell/hold) could also be explored.

## Decision
To implement and compare a comprehensive set of five distinct RL algorithms, spanning different families: value-based (DQN for discrete actions), policy gradient (VPG for both discrete and continuous actions), and advanced actor-critic (DDPG, SAC for continuous actions).

## Consequences
This demonstrates a strong command of the RL domain and enables a robust, evidence-based comparison of different approaches for the specific task. The breadth of exploration is a major strength. The negative consequence is the increased complexity and maintenance burden associated with managing multiple, distinct algorithmic codebases.
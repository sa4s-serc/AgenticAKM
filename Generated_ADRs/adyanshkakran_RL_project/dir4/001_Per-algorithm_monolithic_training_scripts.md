# ADR-001: Per-algorithm, monolithic training scripts

**Date**: 2025-10-14
**Status**: Proposed

## Context
Repository contains standalone DQN.py, DDPG.py, SAC.py, VPG-discrete.py, VPG-continuous.py that each handle data loading, env wiring, agent setup, training, logging, and checkpointing.

## Decision
Implement a script-per-algorithm architecture with end-to-end pipelines rather than a shared training framework or reusable trainer modules.

## Consequences
Pros: fast iteration, clear entry points, low coupling; Cons: code duplication, inconsistent features across algorithms, harder refactors, higher maintenance burden and risk of configuration drift.
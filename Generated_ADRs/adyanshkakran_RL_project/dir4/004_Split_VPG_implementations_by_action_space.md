# ADR-004: Split VPG implementations by action space

**Date**: 2025-10-14
**Status**: Proposed

## Context
Presence of VPG-discrete.py and VPG-continuous.py; other algorithms map naturally to discrete/continuous (DQN for discrete, DDPG/SAC for continuous).

## Decision
Handle discrete vs. continuous action spaces via separate implementations rather than a unified policy interface.

## Consequences
Simplifies each implementation and reduces conditionals; leads to duplication of training logic and diverging feature sets, making maintenance and experiment parity harder.
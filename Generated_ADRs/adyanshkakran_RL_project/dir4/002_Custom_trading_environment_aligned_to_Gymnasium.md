# ADR-002: Custom trading environment aligned to Gymnasium

**Date**: 2025-10-14
**Status**: Proposed

## Context
env.py defines/adapts a portfolio/trading environment; requirements include Gymnasium and gym-trading-env; algorithms interoperate across environments.

## Decision
Design the trading environment to follow the Gymnasium API so it can be consumed by multiple RL algorithms with minimal glue.

## Consequences
Enables algorithm reuse and benchmarking parity; simplifies logging/evaluation tooling; but requires careful reward/observation design, validation against market conventions, and robust preprocessing to avoid leakage.
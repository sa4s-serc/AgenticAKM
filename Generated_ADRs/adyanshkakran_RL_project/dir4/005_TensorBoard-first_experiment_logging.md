# ADR-005: TensorBoard-first experiment logging

**Date**: 2025-10-14
**Status**: Proposed

## Context
logs/ contains TensorBoard event files organized by run names and train/ subfolders; testing_rewards.txt and stats CSVs exist.

## Decision
Use TensorBoard event files as the primary training telemetry, complemented by lightweight CSV summaries.

## Consequences
Gives broad compatibility and easy visualization; minimal overhead; but lacks structured experiment metadata, making large-scale comparison and automated analytics harder without additional tooling.
# ADR-003: Energy-aware adaptation using dynamic thresholds and recovery cycles

**Date**: 2025-10-09
**Status**: Proposed

## Context
Adaptation must balance energy and accuracy while avoiding oscillations when metrics fluctuate.

## Decision
Analyse computes a dynamic energy threshold and enforces a recovery-cycle stabilization period before allowing another switch.

## Consequences
Reduces thrashing and promotes stable operation; aligns energy use with recent conditions. Risk of delayed response to genuine drift during recovery; requires careful threshold tuning.
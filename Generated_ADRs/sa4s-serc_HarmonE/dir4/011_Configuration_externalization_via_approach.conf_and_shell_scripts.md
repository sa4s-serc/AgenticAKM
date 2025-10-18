# ADR-011: Configuration externalization via approach.conf and shell scripts

**Date**: 2025-10-09
**Status**: Proposed

## Context
Operational strategies (e.g., switching/retraining policies) must be configurable without code changes.

## Decision
Store approach-level configuration in approach.conf and apply via set_approach.sh; include cleanup.sh for artifact management.

## Consequences
Improves operability and reproducibility of experiments. Shell-based configuration is platform-biased and limited compared to structured config management or feature flags.
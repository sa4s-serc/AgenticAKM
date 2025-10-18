# ADR-008: Operational lifecycle via shell wrappers

**Date**: 2025-10-14
**Status**: Proposed

## Context
run.sh and stop.sh are included alongside Docker/Compose files.

## Decision
Provide simple bash scripts to standardize common start/stop workflows.

## Consequences
- Lower barrier for contributors; consistent local commands
- Introduces POSIX shell dependency; potential Windows compatibility issues
- Scripts can encode environment conventions but may drift from docs if not maintained
- Good anchor points for CI/CD job steps
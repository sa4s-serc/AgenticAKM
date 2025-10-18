# ADR-006: Strict dependency pinning in requirements.txt

**Date**: 2025-10-14
**Status**: Proposed

## Context
All Python dependencies are pinned to exact versions.

## Decision
Use fully pinned versions to ensure deterministic builds.

## Consequences
- High reproducibility across machines and CI/CD
- Security updates require deliberate upgrades; potential for lag and known CVEs persisting
- Reduced risk of surprise breakages from upstream changes
- Encourages periodic dependency review and renovation workflows
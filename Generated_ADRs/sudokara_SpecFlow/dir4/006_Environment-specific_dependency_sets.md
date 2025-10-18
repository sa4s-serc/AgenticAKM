# ADR-006: Environment-specific dependency sets

**Date**: 2025-10-14
**Status**: Proposed

## Context
Edge and cloud roles, and different accelerators, require distinct libraries and drivers.

## Decision
Maintain separate requirements files for cloud, edge, and edge variants (CPU/GPU/NPU) plus an all-in-one development list.

## Consequences
Improves install reliability and reduces bloat per target; increases maintenance effort and the risk of version drift across files.
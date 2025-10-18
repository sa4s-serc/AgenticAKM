# ADR-008: In-code configuration instead of external config

**Date**: 2025-10-14
**Status**: Proposed

## Context
No centralized configuration file is present; parameters and paths appear to be defined in code or defaults.

## Decision
Embed hyperparameters, paths, and other settings directly in the codebase.

## Consequences
Reduces setup friction and complexity, but hinders reproducibility, experiment management, and portability across datasets and environments.
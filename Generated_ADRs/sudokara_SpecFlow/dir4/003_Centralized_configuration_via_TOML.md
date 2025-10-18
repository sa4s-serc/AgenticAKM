# ADR-003: Centralized configuration via TOML

**Date**: 2025-10-14
**Status**: Proposed

## Context
Edge and cloud services must share consistent settings while allowing environment variability.

## Decision
Use config.toml with a typed loader/validator in common/config.py as a single source of truth for both sides.

## Consequences
Improves reproducibility and reduces drift across components; requires robust validation, secrets management, and clear override mechanisms for deployment-specific values.
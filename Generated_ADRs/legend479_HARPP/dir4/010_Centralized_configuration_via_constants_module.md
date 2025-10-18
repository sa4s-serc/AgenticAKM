# ADR-010: Centralized configuration via constants module

**Date**: 2025-10-13
**Status**: Proposed

## Context
constants.py is present to centralize constants/configuration values.

## Decision
Collect configuration and magic numbers in a dedicated constants module.

## Consequences
Improves maintainability and discoverability of configuration, easing adjustments and promoting reuse; excessive global constants can encourage implicit coupling if not carefully scoped.
# ADR-002: No packaging or dependency metadata

**Date**: 2025-10-16
**Status**: Proposed

## Context
There are no requirements.txt, pyproject.toml, or setup.py files.

## Decision
Omit formal dependency and packaging configuration and rely on the system Python and manual installation of any libraries.

## Consequences
Lower upfront overhead, but poor environment reproducibility, harder onboarding, challenging distribution or installation, and increased risk of runtime ImportErrors.
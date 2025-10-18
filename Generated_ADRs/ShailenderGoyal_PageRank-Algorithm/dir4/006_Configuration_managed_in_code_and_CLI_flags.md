# ADR-006: Configuration managed in code and CLI flags

**Date**: 2025-10-16
**Status**: Proposed

## Context
Any configuration is defined within project.py (e.g., via argparse) and documented in README; no external config files are present.

## Decision
Use in-code defaults and command-line arguments for configuration instead of external configuration files.

## Consequences
Reduces complexity and deployment friction, but decreases flexibility for environment-specific settings and complicates repeatable runs across contexts.
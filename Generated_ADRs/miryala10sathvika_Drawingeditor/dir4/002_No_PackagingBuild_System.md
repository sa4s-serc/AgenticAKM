# ADR-002: No Packaging/Build System

**Date**: 2025-10-13
**Status**: Proposed

## Context
The repo lacks packaging files (setup.py/pyproject.toml) and has a flat layout of standalone Python files.

## Decision
Treat the codebase as script-style modules executed directly from source rather than an installable package.

## Consequences
Cannot publish or version as a package, harder reuse via imports, no console entry points, and growth beyond a few scripts becomes cumbersome.
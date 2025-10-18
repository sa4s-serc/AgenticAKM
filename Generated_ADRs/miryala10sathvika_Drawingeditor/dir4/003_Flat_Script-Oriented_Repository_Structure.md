# ADR-003: Flat, Script-Oriented Repository Structure

**Date**: 2025-10-13
**Status**: Proposed

## Context
Two Python files (draw.py, extra.py) are at the repo root with no package directories.

## Decision
Keep a minimal, flat structure without module/package boundaries.

## Consequences
Simplicity for small scope, but poor scalability, higher risk of name collisions, unclear ownership/separation of concerns, and harder refactoring into larger components.
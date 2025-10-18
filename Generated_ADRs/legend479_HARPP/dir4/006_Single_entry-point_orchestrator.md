# ADR-006: Single entry-point orchestrator

**Date**: 2025-10-13
**Status**: Proposed

## Context
main.py is identified as the application entry point and coordinator for interaction and UI.

## Decision
Centralize startup, dependency wiring, and high-level coordination in main.py.

## Consequences
Simplifies bootstrapping and provides a clear execution entry, but may evolve into a "god object" if orchestration, business logic, and UI concerns accumulate without further delegation.
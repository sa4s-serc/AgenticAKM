# ADR-001: Monolithic single-script architecture

**Date**: 2025-10-16
**Status**: Proposed

## Context
The repository contains a single executable Python file (project.py) and a README, with no modules or packages.

## Decision
Implement all core logic, I/O, and any CLI directly within a single Python script that serves as the entry point.

## Consequences
Simple to run and easy to comprehend for small scope, but limited maintainability and testability, weaker separation of concerns, and higher refactor cost as functionality grows.
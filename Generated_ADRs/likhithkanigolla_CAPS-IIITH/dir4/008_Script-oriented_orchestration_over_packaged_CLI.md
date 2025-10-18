# ADR-008: Script-oriented orchestration over packaged CLI

**Date**: 2025-10-09
**Status**: Proposed

## Context
Users need straightforward entry points to run generation and visualization tasks during research/prototyping.

## Decision
Expose top-level scripts (generate_pydevs.py, generator/main_generator.py, llmbased/main.py, web_generator.py) rather than a unified installable CLI package.

## Consequences
Lowers barrier to experimentation; simplifies debugging; trades off standardized installation and dependency management; risks environment drift across scripts.
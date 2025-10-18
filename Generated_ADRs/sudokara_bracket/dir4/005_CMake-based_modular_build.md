# ADR-005: CMake-based modular build

**Date**: 2025-10-14
**Status**: Proposed

## Context
Cross-platform support and module-level build configuration are needed for a growing codebase.

## Decision
Use CMake with per-module CMakeLists.txt files and an aggregate lib/CMakeLists.txt to orchestrate builds.

## Consequences
Supports scalable builds, clear ownership per module, and straightforward integration with IDEs and CI. Increases build configuration surface area that must be maintained consistently across modules.
# ADR-015: Lightweight orchestration via shell and Python scripts without formal dependency management

**Date**: 2025-10-10
**Status**: Proposed

## Context
Running the system requires a simple command path, but environment setup must be handled by users.

## Decision
Orchestrate with command.sh and App.py and document setup in the README without a standardized dependency file.

## Consequences
Low entry barrier and fewer moving parts, but higher risk of environment drift, setup friction, and challenges in CI/CD, containerization, and reproducible deployments.
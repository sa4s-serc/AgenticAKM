# ADR-006: Externalized Configuration and Target-Specific Dependencies

**Date**: 2025-10-14
**Status**: Proposed

## Context
The system must be deployed in various environments with different model choices, network settings, and hardware. Hardcoding these parameters would make the system inflexible and difficult to manage.

## Decision
System parameters are externalized into a `config.toml` file, and environment-specific Python dependencies are split into multiple files (e.g., `requirements-cloud.txt`, `requirements-edge-cpu.txt`).

## Consequences
This approach enhances maintainability and simplifies deployment, allowing configuration changes without altering code. It also minimizes the dependency footprint for each specific target. However, it requires careful management to keep the multiple requirements files and configuration options documented and synchronized.
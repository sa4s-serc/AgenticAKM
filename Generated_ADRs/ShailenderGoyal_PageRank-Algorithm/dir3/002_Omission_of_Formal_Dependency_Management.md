# ADR-002: Omission of Formal Dependency Management

**Date**: 2025-10-16
**Status**: Proposed

## Context
The repository is structured as a simple, standalone project, potentially developed and used within a controlled environment where necessary libraries were assumed to be present.

## Decision
No standard dependency management file, such as `requirements.txt` or `pyproject.toml`, was included to explicitly declare external libraries.

## Consequences
This choice keeps the project structure clean with a minimum number of files. Critically, it impairs reproducibility and creates a significant barrier for new users, who must manually infer and install the correct dependencies and versions, leading to potential setup friction and runtime errors.
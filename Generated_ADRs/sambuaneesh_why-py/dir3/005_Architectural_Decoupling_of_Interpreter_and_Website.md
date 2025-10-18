# ADR-005: Architectural Decoupling of Interpreter and Website

**Date**: 2025-10-11
**Status**: Proposed

## Context
The project consists of two fundamentally different components: a Python-based backend interpreter and a Node.js-based frontend documentation site. A strategy was needed to manage their distinct technological and developmental needs.

## Decision
A clean architectural separation was maintained by housing the Python interpreter at the project root and the Node.js/Astro website within its own `documentation/` subdirectory. Each part has its own dependency management and build processes.

## Consequences
This decoupling allows each component to evolve independently using the best tools for its respective domain (Python for the interpreter, Node.js for the web). It simplifies the development workflow, CI/CD pipelines, and dependency management, preventing technological entanglement.
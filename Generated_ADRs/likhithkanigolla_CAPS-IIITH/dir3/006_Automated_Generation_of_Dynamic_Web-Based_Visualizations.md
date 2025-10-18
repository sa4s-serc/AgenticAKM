# ADR-006: Automated Generation of Dynamic Web-Based Visualizations

**Date**: 2025-10-09
**Status**: Proposed

## Context
Text-based logs and console output are often insufficient for understanding the complex, dynamic behavior of a running simulation. A more intuitive, visual method was desired to allow users to observe component states and interactions in real-time.

## Decision
A dedicated web generator was developed to produce a complete, self-contained visualization frontend (HTML, CSS, JavaScript) from the same intermediate JSON model used for Python code generation. This provides a dynamic, graphical representation of the running simulation.

## Consequences
This feature dramatically improves the usability and observability of the generated simulations, adding significant value for the end-user. It also showcases the power of the intermediate representation architecture. However, it introduces web development technologies into the project, expanding the required skill set and increasing the overall system complexity.
# ADR-004: Dependency Management Strategy

**Date**: 2025-10-13
**Status**: Proposed

## Context
A decision was needed on whether to leverage third-party libraries to accelerate development or to rely solely on the standard library to ensure simplicity and portability.

## Decision
A 'zero-dependency' approach was adopted. The entire application is built using only Python and its standard libraries (`tkinter`, `xml`). No external packages are required.

## Consequences
The primary benefit is extreme simplicity in distribution and setup; a user only needs a standard Python installation to run the application. This eliminates complexities related to package managers and virtual environments. The trade-off is that the project cannot leverage the powerful, feature-rich, and often more performant libraries available in the Python ecosystem for graphics, UI, or data handling, forcing the developers to implement all functionality from scratch.
# ADR-001: Adoption of an MVC-like Architectural Pattern

**Date**: 2025-10-13
**Status**: Proposed

## Context
The application required a structured design to separate the user interface from the core business logic and data models. This separation is essential for managing complexity, enhancing maintainability, and allowing components to be developed and tested independently.

## Decision
An architecture resembling the Model-View-Controller (MVC) pattern was implemented. The View (`window.py`) handles GUI presentation, the Controller (`main.py`) manages the event loop and application flow, and the Model (`shapes.py`, `object.py`) represents the application's data and business rules.

## Consequences
This decision leads to a highly modular and decoupled system. It simplifies maintenance, as changes to the UI have minimal impact on the core logic. However, it introduces a level of indirection that might add slight complexity for trivial features.
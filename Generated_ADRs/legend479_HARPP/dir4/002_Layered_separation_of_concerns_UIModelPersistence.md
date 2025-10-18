# ADR-002: Layered separation of concerns (UI–Model–Persistence)

**Date**: 2025-10-13
**Status**: Proposed

## Context
The codebase splits responsibilities across window.py (UI), shapes.py/group.py/object.py (model), export.py (persistence), and main.py (coordination).

## Decision
Adopt a modular separation akin to MVC: UI in window.py, domain model in shapes/group/object modules, persistence isolated in export.py, with main.py orchestrating interactions.

## Consequences
Improves maintainability and testability by isolating concerns and allowing targeted changes; however, without an explicit controller layer, coordination logic may drift into UI or main.py, risking tighter coupling.
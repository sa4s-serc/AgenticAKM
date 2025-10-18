---
### ADR-003: Adopt the Composite pattern for shapes and groups

**Status:** Inferred
**Context:** The source contains object.py (likely a base abstraction), shapes.py (concrete shapes), and group.py (grouping behavior). A drawing editor commonly needs to treat single shapes and groups uniformly for operations like move, resize, select, and export.
**Decision:** Implement a base drawable object with concrete shapes and a group entity that composes multiple objects, enabling uniform operations via the Composite pattern.
**Consequences:** 
- Positive: Simplifies client code (uniform handling of shapes and groups), enables nested grouping, eases bulk operations and export.
- Negative: Increases abstraction complexity, requires careful handling of transformations and hit-testing across hierarchies.
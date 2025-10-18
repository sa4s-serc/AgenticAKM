---
### ADR-004: Separate UI layer from domain logic (MVC/MVP-style separation)

**Status:** Inferred
**Context:** The presence of window.py (UI concerns) and separate modules for domain logic (shapes.py, group.py, object.py, export.py) suggests a layered approach. Test coverage exists for shapes independent of the UI (tests/test_shapes.py).
**Decision:** Keep UI/event handling concerns in window.py (and orchestration in main.py), while encapsulating domain logic in separate modules. Use a controller-like main entry to coordinate between UI and model.
**Consequences:** 
- Positive: Improved testability, clearer separation of concerns, easier maintenance of domain logic independent of UI.
- Negative: Requires careful API design between layers; potential for duplication of state or event mapping if not managed well.
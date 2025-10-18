---
### ADR-008: Single entry point with an event-driven main loop

**Status:** Inferred
**Context:** main.py is present, and sequence diagrams for Edit and Save imply event-driven flows. PySimpleGUI typically uses a central event loop that dispatches actions based on UI events.
**Decision:** Implement a single application entry point (main.py) that owns the event loop, dispatching user actions to domain logic (e.g., edit operations, export).
**Consequences:** 
- Positive: Clear control flow, straightforward orchestration of UI and domain interactions.
- Negative: Risk of accumulating monolithic logic in main if responsibilities aren’t well-factored; careful error handling required to keep the UI responsive.
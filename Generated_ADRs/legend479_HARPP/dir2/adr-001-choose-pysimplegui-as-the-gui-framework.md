### ADR-001: Choose PySimpleGUI as the GUI framework

**Status:** Inferred
**Context:** The project is a drawing editor with interactive UI requirements. The presence of window.py suggests a dedicated UI layer, and requirements.txt lists PySimpleGUI, indicating a need for a simple, cross-platform way to build windows and handle events without the complexity of lower-level toolkits.
**Decision:** Use PySimpleGUI to implement the application window, event loop, and interactive controls.
**Consequences:** 
- Positive: Rapid UI development, simpler event handling, cross-platform support, minimal boilerplate.
- Negative: Limited customization and performance compared to lower-level frameworks; dependency on PySimpleGUI’s abstractions and release cadence.
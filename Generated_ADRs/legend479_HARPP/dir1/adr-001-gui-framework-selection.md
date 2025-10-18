### ADR-001: GUI Framework Selection

**Status:** Inferred
**Context:** The project is a "Drawing Editor," which inherently requires a graphical user interface (GUI) to allow users to create, view, and manipulate shapes. A decision was needed on which Python library to use for building this user-facing component, balancing development speed, features, and complexity.
**Decision:** The project will use `PySimpleGUI` as its primary GUI framework. This is directly evidenced by its inclusion as a dependency in the `requirements.txt` file and supported by the presence of `src/window.py`, which is a common pattern for managing the main application window.
**Consequences:**
*   **Positive:** `PySimpleGUI` is known for its simplicity and allows for rapid development of user interfaces. This choice likely accelerated the initial development of the editor's UI. It abstracts away the complexities of underlying toolkits like Tkinter or Qt.
*   **Negative:** The application's UI is now dependent on the features and limitations of `PySimpleGUI`. This may restrict the implementation of highly custom or complex UI components compared to more powerful, lower-level frameworks. Performance might be a concern for very complex drawings with many objects.
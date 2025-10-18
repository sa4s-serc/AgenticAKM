---
### ADR-002: Data Persistence and Export Format

**Status:** Inferred
**Context:** The drawing editor needs a way to save the user's work to a file and potentially load it back. This requires a structured data format that can represent the various shapes, their properties (color, position, size), and their relationships (e.g., groups).
**Decision:** XML (eXtensible Markup Language) was chosen as the data format for saving and exporting drawings. This is inferred from the `xml-python` dependency in `requirements.txt` and corroborated by the existence of `src/export.py` and a design document named `SequenceDiagramSave.jpeg`.
**Consequences:**
*   **Positive:** XML is a well-established, human-readable standard. This makes debugging saved files easier. Its hierarchical nature is well-suited for representing a scene graph of shapes and groups. A wide range of parsers and tools are available for it.
*   **Negative:** XML is often more verbose than other formats like JSON or binary formats, which can lead to larger file sizes. Parsing XML can be more computationally intensive than for more compact formats.
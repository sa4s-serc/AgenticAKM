---
### ADR-002: Data Persistence and Configuration Strategy

**Status:** Inferred
**Context:** The application needs to store or retrieve data that may vary in structure and complexity. A decision was needed on which file formats to use for this purpose, balancing ease of parsing, human readability, and the ability to represent structured information.
**Decision:** A multi-format strategy was adopted for data persistence. Plain text (`.txt`) is used for simple or unstructured data (`kas.txt`), while XML (`.xml`) is used for data requiring a hierarchical structure and formal schema (`kavin.xml`).
**Consequences:**
*   **Positive:** Allows for selecting the most appropriate format for the specific type of data (simplicity for `.txt`, structure and validation for `.xml`).
*   **Negative:** The application's codebase must include logic to parse and handle multiple distinct file formats, which can increase complexity compared to standardizing on a single format (e.g., JSON or YAML).
*   **Trade-off:** The benefits of format-specific features (like XML's verbosity and schema support) were valued more than the simplicity of a single, unified data format.
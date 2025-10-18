---
### ADR-002: Use XML as the persistence/export format

**Status:** Inferred
**Context:** The repository includes export.py and a Save sequence diagram, and requirements.txt includes xml-python. This indicates the need to serialize drawings to a portable and human-readable format that can encode shapes and their relationships.
**Decision:** Persist drawings in XML using the xml-python library to serialize/deserialize drawing objects and groups.
**Consequences:** 
- Positive: Human-readable, widely interoperable, schema-friendly, good for structured hierarchical data (e.g., groups of shapes).
- Negative: Verbose files, potential performance overhead vs. binary formats, need to manage schemas/versions to ensure backward compatibility.
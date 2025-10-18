---
### ADR-004: Store ancillary data as plain text files

**Status:** Inferred
**Context:** The repository includes kas.txt, implying some data/resources are kept as raw text.
**Decision:** Use plain text files for simple, unstructured auxiliary data.
**Consequences:** 
- Positive: Human-readable, easy to create/edit with basic tools, no specialized parsers required.
- Negative: No inherent schema or validation, potential ambiguity in encoding/format, harder to evolve if structure becomes more complex.
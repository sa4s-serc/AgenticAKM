---
### ADR-004: Conform to Azure Cognitive Search custom skill input/output schema

**Status:** Inferred
**Context:** Custom skills must implement a defined JSON contract (array of records in, array of records out) to interoperate with Azure Cognitive Search skillsets.
**Decision:** Design the function to accept and return the standard custom skill JSON schema, enabling batch processing of records.
**Consequences:** 
- Positive: Seamless integration into skillsets; supports batch processing; predictable contract for callers.
- Negative: Must handle per-record failures gracefully; payload size limits apply; additional serialization/deserialization logic.
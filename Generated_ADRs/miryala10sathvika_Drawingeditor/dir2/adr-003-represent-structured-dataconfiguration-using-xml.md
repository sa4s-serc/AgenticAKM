---
### ADR-003: Represent structured data/configuration using XML

**Status:** Inferred
**Context:** The presence of kavin.xml indicates that at least some structured data or configuration is stored in XML.
**Decision:** Use XML for structured configuration/data representation.
**Consequences:** 
- Positive: Strong support for hierarchical/structured data, schema validation possible (XSD), mature tooling.
- Negative: Verbose compared to JSON/YAML, more cumbersome to edit manually, requires XML parsing libraries and care with namespaces.
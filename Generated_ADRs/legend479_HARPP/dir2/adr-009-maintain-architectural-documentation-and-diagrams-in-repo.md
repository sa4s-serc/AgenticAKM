---
### ADR-009: Maintain architectural documentation and diagrams in-repo

**Status:** Inferred
**Context:** The repo includes a Design Document, Class Diagram, and Sequence Diagrams for Edit and Save under doc/. This reflects a deliberate choice to document architecture alongside code.
**Decision:** Keep architecture and design documents (PDFs, diagrams) versioned with the source code to guide implementation and onboarding.
**Consequences:** 
- Positive: Shared understanding, easier onboarding, alignment between design and implementation, historical trace of decisions.
- Negative: Ongoing maintenance required to keep documents in sync with the code; potential duplication of knowledge if not curated.
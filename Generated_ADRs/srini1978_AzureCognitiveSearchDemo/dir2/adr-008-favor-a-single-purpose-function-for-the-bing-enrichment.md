---
### ADR-008: Favor a single-purpose function for the Bing enrichment

**Status:** Inferred
**Context:** The project contains a single function source file (BingCustomSearch.cs), implying a focused responsibility.
**Decision:** Implement a single, focused function dedicated to Bing Custom Search enrichment rather than a multi-function app.
**Consequences:** 
- Positive: Simpler codebase; easier to reason about, test, and secure; minimal blast radius for changes.
- Negative: May require additional functions/projects if future enrichment types are added; potential duplication across separate functions.
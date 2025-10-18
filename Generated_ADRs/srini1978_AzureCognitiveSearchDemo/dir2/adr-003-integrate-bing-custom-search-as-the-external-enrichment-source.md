---
### ADR-003: Integrate Bing Custom Search as the external enrichment source

**Status:** Inferred
**Context:** The custom skill named BingCustomSearch suggests using Microsoft’s Bing Custom Search API to augment or derive information during enrichment.
**Decision:** Call Bing Custom Search from the custom skill to retrieve or enrich content as part of the indexing pipeline.
**Consequences:** 
- Positive: High-quality web search scoped by custom configurations, improved enrichment with external knowledge.
- Negative: External API dependency introduces latency, potential throttling, and cost; requires managing API keys and error handling.
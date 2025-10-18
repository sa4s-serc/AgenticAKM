---
### ADR-003: Implement an Extensible Data Enrichment Pipeline

**Status:** Inferred
**Context:** The standard indexing process may not be sufficient to extract all the required information from the source documents. There is a need to augment the data during ingestion with information from external sources. The file `Customskills/BingCustomSearch.cs` indicates a specific requirement to enrich content by querying an external web search API.
**Decision:** The data ingestion process will be designed as an extensible pipeline using Azure Cognitive Search Skillsets. This allows for the integration of custom skills that call external APIs. Specifically, a custom skill was developed to call the Bing Custom Search API to find related information and add it to the search index alongside the original document content.
**Consequences:**
*   **Positive:**
    *   The search index becomes more valuable as it's enriched with external, contextual data.
    *   The architecture is flexible and allows for adding more custom skills in the future to connect to other APIs or perform complex transformations.
    *   Leverages the power of a specialized external service (Bing) instead of trying to replicate its functionality.
*   **Negative:**
    *   Introduces an external dependency on the Bing Custom Search API, which could be a point of failure or a performance bottleneck.
    *   Increases the overall cost of the solution due to API usage fees.
    *   Adds latency to the indexing process as each document requires an external network call.
### ADR-001: Host the custom enrichment as an Azure Function (serverless)

**Status:** Inferred
**Context:** The solution needs to provide a custom enrichment step for an Azure Cognitive Search skillset. This requires an HTTP-accessible endpoint that adheres to the custom skill contract and can scale with indexing workloads while remaining easy to develop and deploy.
**Decision:** Implement the custom skill as an Azure Function, using the Azure Functions runtime (presence of host.json, local.settings.json) and an HTTP-triggered function.
**Consequences:** 
- Positive: Serverless scaling, consumption-based cost, straightforward local development and deployment, native JSON/HTTP support, easy integration with Azure Cognitive Search.
- Negative: Potential cold starts, opaque scaling limits under heavy batch loads, need to manage function app configuration and monitoring.
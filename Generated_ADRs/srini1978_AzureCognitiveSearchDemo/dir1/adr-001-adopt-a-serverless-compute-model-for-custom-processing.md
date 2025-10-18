### ADR-001: Adopt a Serverless Compute Model for Custom Processing

**Status:** Inferred
**Context:** The system requires custom logic to be executed during the data processing pipeline. A key architectural challenge is how to host and execute this custom code without the overhead of managing dedicated virtual machines or servers. The solution needs to be scalable, cost-effective, and integrate well with other cloud services. The presence of `host.json` and `local.settings.json` files are strong indicators of a specific serverless platform being considered.
**Decision:** The project will use Azure Functions to host and run custom code. The C# project (`CustomSkillset.csproj`, `BingCustomSearch.cs`) will be deployed as an Azure Function, which can be invoked via HTTP requests.
**Consequences:**
*   **Positive:**
    *   Reduces operational overhead as there is no server infrastructure to manage.
    *   Provides automatic scaling based on demand.
    *   The pay-per-use pricing model is cost-effective for workloads with variable traffic.
    *   Seamless integration with the Azure ecosystem, particularly Azure Cognitive Search.
*   **Negative:**
    *   Potential for "cold starts," which can introduce latency for the first request after a period of inactivity.
    *   Execution time and resource limits are imposed by the platform, which may not be suitable for very long-running tasks.
    *   Increased dependency on the Azure platform (vendor lock-in).
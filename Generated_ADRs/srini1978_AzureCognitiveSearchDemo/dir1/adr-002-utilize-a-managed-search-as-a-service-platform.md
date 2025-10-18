---
### ADR-002: Utilize a Managed Search-as-a-Service Platform

**Status:** Inferred
**Context:** The project needs to make a large and diverse set of documents (`.pdf`, `.docx`, `.pptx`, `.html`, etc.) searchable. The challenge is to build a robust search solution that can ingest, index, and query these various formats without building a search engine from scratch. The folder name `Customskills` and the project name `CustomSkillset.csproj` are specific terms associated with a particular search technology.
**Decision:** The architecture will be centered around Azure Cognitive Search. This managed service will be used to create and manage the search index, orchestrate the data ingestion pipeline, and handle query execution. The custom code implemented in the repository is designed as a "Custom Skill" to be plugged into this pipeline.
**Consequences:**
*   **Positive:**
    *   Significantly accelerates development by providing a fully-featured search engine out-of-the-box.
    *   Built-in capabilities for indexing various document formats found in the `sampledocs` directory.
    *   Provides a clear extension point (the "skillset") for injecting custom data enrichment and transformation logic.
    *   The service is managed, highly available, and scalable.
*   **Negative:**
    *   The cost can be significant, scaling with the amount of data, number of indexes, and query volume.
    *   Configuration and management of the indexing pipeline can be complex.
    *   Creates a strong architectural dependency on the Azure Cognitive Search service.
---
### ADR-004: Adherence to an OpenAI-Compatible API using FastAPI

**Status:** Inferred

**Context:** To ensure broad adoption and seamless integration with existing client applications and developer tools, the LLM serving engine must expose its functionality through a familiar, industry-standard API. The API server also needs to be performant, scalable, and capable of handling many concurrent connections efficiently.

**Decision:** The system provides an API server built with FastAPI that is compatible with the OpenAI API specification. This is clearly indicated by the `sarathi/entrypoints/openai/` module, which contains an `api_server.py`, protocol definitions, and serving logic. The inclusion of `fastapi`, `uvicorn`, and `openai` in `requirements.txt` confirms the choice of this modern, high-performance web framework for serving an OpenAI-compliant endpoint.

**Consequences:**
*   **Positive:**
    *   Clients and tools built for the OpenAI API can use this system with minimal to no modification, dramatically lowering the barrier to entry.
    *   FastAPI provides excellent performance, built-in support for asynchronous operations, automatic API documentation, and data validation.
*   **Negative:**
    *   The system's public interface is now coupled to an external specification (OpenAI's API), requiring maintenance to stay in sync with any changes or updates to that standard.
    *   It may limit the ability to expose unique, non-standard features of the serving engine through the primary API.
---
### ADR-005: Integration with Google Generative AI for Core Intelligence

**Status:** Inferred
**Context:** The application's core value proposition involves understanding and transforming user-provided documents (PDFs) into various content formats. This requires sophisticated natural language processing and generation capabilities.
**Decision:** To use a third-party Large Language Model (LLM) service provided by Google. This is explicitly shown by the `google-genai` dependency in `requirements.txt` and the `backend/llm.py` module, which likely abstracts the interaction with this service.
**Consequences:**
*   **Positive:**
    *   **State-of-the-Art AI:** The application leverages powerful, pre-trained models without the immense cost and complexity of training and hosting them in-house.
    *   **Rapid Feature Development:** Enables rapid development of AI-powered features like summarization, script generation (for reels), and chat-based interaction.
*   **Negative:**
    *   **Vendor Lock-in:** The application becomes dependent on Google's AI services, making it potentially difficult or costly to switch providers in the future.
    *   **Operational Cost:** Usage of the API will incur costs based on consumption, which needs to be monitored and managed.
    *   **External Dependency:** The application's performance and availability are tied to the uptime and latency of Google's external service.
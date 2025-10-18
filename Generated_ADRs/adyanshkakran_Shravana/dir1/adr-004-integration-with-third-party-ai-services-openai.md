---
### ADR-004: Integration with Third-Party AI Services (OpenAI)

**Status:** Inferred
**Context:** The application required advanced capabilities related to natural language processing and/or speech recognition to power its features, particularly for the conversational bot. Developing these complex AI models from scratch would be prohibitively expensive and time-consuming.
**Decision:** The system integrates with the OpenAI API for AI-powered features. This is strongly indicated by the `openai` library in `requirements.txt`, the `openai/service.py` file, the `asr.py` (Automatic Speech Recognition) file, and the temporary `.ogg` audio files in the `instance/` directory.
**Consequences:**
*   **Positive:**
    *   **State-of-the-Art Capabilities:** Provides access to powerful, pre-trained AI models without the need for in-house ML expertise or infrastructure.
    *   **Faster Time-to-Market:** Enables the rapid implementation of sophisticated features like chatbots, text summarization, or speech-to-text.
*   **Negative:**
    *   **External Dependency:** The system is reliant on OpenAI's availability, performance, and pricing. Any outage or policy change from OpenAI can directly impact the application.
    *   **Data Privacy:** User data (e.g., audio recordings, text messages) is sent to a third-party service, which may have data privacy and security implications.
    *   **Cost:** Usage of the OpenAI API is typically metered, leading to operational costs that scale with user activity.
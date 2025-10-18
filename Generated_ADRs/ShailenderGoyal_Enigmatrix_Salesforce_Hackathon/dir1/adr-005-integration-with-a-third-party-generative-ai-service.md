---
### ADR-005: Integration with a Third-Party Generative AI Service

**Status:** Inferred
**Context:** A core requirement of the "AI-buddy" application is to provide intelligent, AI-powered features. The project faced a build-vs-buy decision: develop a proprietary AI model or integrate with an existing, powerful external service.
**Decision:** The architecture integrates with an external, third-party AI service provided by Google. This is evident from the `@google/generative-ai` dependency in the backend and the presence of dedicated `ai.controller.js` and `ai.route.js` files, which abstract the AI logic behind the server's API.
**Consequences:**
*   **Positive:** This decision allows the application to leverage state-of-the-art AI capabilities without the massive investment in research, training, and infrastructure required to build a proprietary model. It enables faster development of AI-powered features.
*   **Negative:** The application is now dependent on an external service, introducing a potential single point of failure and vendor lock-in. API usage will incur operational costs that scale with user activity. Network latency to the external service could impact the responsiveness of AI features.
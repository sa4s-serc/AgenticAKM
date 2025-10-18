---
### ADR-006: Conversational Interface via WhatsApp Bot

**Status:** Inferred
**Context:** The project aimed to provide a user interface that is highly accessible and familiar to a broad audience, reducing the friction of downloading and learning a new application for certain tasks.
**Decision:** A WhatsApp bot was implemented as a primary channel for user interaction. This is directly implied by the `whatsapp-bot` directory name and further supported by the `meta/webhook.py` file. Webhooks are the standard mechanism for integrating with the Meta (WhatsApp Business) API.
**Consequences:**
*   **Positive:**
    *   **Massive User Reach:** Leverages the huge existing user base of WhatsApp, making the service instantly accessible to billions of people.
    *   **Low Friction:** Users can interact with the service without installing a separate app, using an interface they are already comfortable with.
    *   **Push Notifications:** The platform is inherently suited for sending notifications and asynchronous updates to users.
*   **Negative:**
    *   **Platform Dependency:** The functionality is entirely dependent on the WhatsApp Business Platform, including its features, limitations, API policies, and pricing.
    *   **Constrained UI/UX:** The user experience is limited to the conversational components and formats supported by WhatsApp (text, buttons, lists, media).
    *   **Complex State Management:** Managing conversation state and context in a stateless webhook-based system can be challenging.
---
### ADR-005: Flask-based webhook service for WhatsApp bot

Status: Inferred
Context: The backend integrates with the Meta WhatsApp Business API, which relies on webhooks for message delivery and verification. The requirements include Flask, indicating a lightweight Python web server.
Decision: Implement the WhatsApp bot backend using Flask.
Consequences:
- Positive: Simple, lightweight, familiar Python framework; fast to implement webhook endpoints and middleware.
- Negative: Requires careful async strategy (Flask is synchronous by default) or delegation for long-running tasks; scaling considerations under high load.
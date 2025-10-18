---
### ADR-010: Integrate Google Generative AI for AI features

Status: Inferred
Context: The server depends on @google/generative-ai and has an ai.controller.js and ai.route.js; the app features chat, roadmaps, and knowledge assistance.
Decision: Use Google’s Generative AI SDK to power AI-driven features (chat, guidance, knowledge tasks).
Consequences:
- Positive: Rapid AI capability integration; leverages state-of-the-art models.
- Negative: Vendor dependency and cost; latency variability; strict key/quotas management; potential vendor lock-in.
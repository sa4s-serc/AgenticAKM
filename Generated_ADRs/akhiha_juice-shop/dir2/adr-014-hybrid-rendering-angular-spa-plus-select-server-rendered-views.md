---
### ADR-014: Hybrid rendering: Angular SPA plus select server-rendered views

Status: Inferred
Context: views/ contains Pug and Handlebars templates (e.g., promotionVideo.pug, dataErasureForm.hbs), while the SPA handles most UI.
Decision: Use SPA for the main app and server-rendered templates for specific flows/pages where server-side output is simpler or intentional (e.g., forms).
Consequences:
- Positive: Flexibility to implement special pages; simplifies some server-only scenarios.
- Negative: Mixed rendering stack adds complexity; different templating engines to maintain.
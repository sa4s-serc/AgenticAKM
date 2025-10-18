---
### ADR-010: Keep styling minimal with a single CSS file

Status: Inferred
Context: A single style.css is present with no CSS frameworks or preprocessors.
Decision: Use a simple global CSS file for styling needs.
Consequences:
- Positive: Minimal overhead, easy to reason about, no additional build steps.
- Negative: Limited scalability for complex UIs; lacks structure and constraints provided by CSS frameworks or methodologies.
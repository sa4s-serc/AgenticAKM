---
### ADR-009: Organize components by feature with index and styles files

Status: Inferred
Context: Component directories follow a pattern with index.js and *.styles.js (e.g., components/Actor/index.js and Actor.styles.js). Shared UI elements like Button, Grid, and Spinner are modularized.
Decision: Use a per-component folder structure with an index.js entry and a co-located styles file, and factor out reusable UI primitives.
Consequences:
- Positive: Clear boundaries and discoverability; improved reusability; simpler imports; easier incremental scaling of the component library.
- Negative: Slightly more files per component; requires discipline to keep component responsibilities focused.
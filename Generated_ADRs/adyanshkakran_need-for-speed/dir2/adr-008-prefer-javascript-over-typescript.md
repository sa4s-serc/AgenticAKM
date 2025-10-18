---
### ADR-008: Prefer JavaScript over TypeScript

Status: Inferred
Context: No TypeScript configuration or dependencies are present. Source files are .js and the project is configured as "type": "module".
Decision: Use plain JavaScript ES modules instead of TypeScript.
Consequences:
- Positive: Zero compile step for types, reduced tooling, quicker setup and iteration.
- Negative: No static typing or compiler checks; potential increase in runtime errors and reduced developer ergonomics for large-scale refactors.
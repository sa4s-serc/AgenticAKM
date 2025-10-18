---
### ADR-004: Provide a console-based interface as the initial delivery mechanism

Status: Inferred
Context: carbonQLConsole is the only executable in the solution (carbonQLConsole.exe), serving as the user-facing layer.
Decision: Use a console application to run and demonstrate the backend calculations and workflows.
Consequences:
- Positive: Fast to build and run, good for local development, demos, and scripting.
- Negative: Limited UX and integration capabilities; not suitable for broad user access or integration without additional hosts (e.g., web API).
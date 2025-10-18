---
### ADR-002: Split solution into reusable backend library and a console host

Status: Inferred
Context: The solution (carbonQL.sln) contains two projects: carbonQLBackend (class library producing carbonQLBackend.dll) and carbonQLConsole (executable producing carbonQLConsole.exe) which references and ships with carbonQLBackend.dll.
Decision: Place core domain logic in a class library (carbonQLBackend) and provide a console application (carbonQLConsole) as the initial host and entry point.
Consequences:
- Positive: Encourages separation of concerns, enables reuse of backend logic by future hosts (e.g., web API, GUI), simplifies testing of business logic.
- Negative: Adds cross-project coordination and builds; initial users without a console-centric workflow may find it less convenient.
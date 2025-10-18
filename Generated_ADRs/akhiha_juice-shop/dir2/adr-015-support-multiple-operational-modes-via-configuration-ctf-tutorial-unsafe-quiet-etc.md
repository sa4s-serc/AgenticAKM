---
### ADR-015: Support multiple operational modes via configuration (CTF, tutorial, unsafe, quiet, etc.)

Status: Inferred
Context: Multiple config/*.yml files (ctf.yml, tutorial.yml, unsafe.yml, quiet.yml, etc.) and features like a scoreboard indicate mode-driven behavior.
Decision: Implement mode-specific behavior controlled by config profiles to support learning scenarios, CTFs, and demonstrations.
Consequences:
- Positive: Highly flexible for different audiences and training contexts.
- Negative: Increased conditional logic and testing matrix; risk of misconfiguration.
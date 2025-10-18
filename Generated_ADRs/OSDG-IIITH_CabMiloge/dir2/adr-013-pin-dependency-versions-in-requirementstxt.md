---
### ADR-013: Pin Dependency Versions in requirements.txt

Status: Inferred
Context: requirements.txt pins exact versions for all dependencies (Flask, Gunicorn, etc.).
Decision: Use fully pinned dependency versions to ensure reproducible builds.
Consequences: Predictable, repeatable environments and minimized “works on my machine” issues. Requires active maintenance to update versions and patch vulnerabilities; can accumulate tech debt if not refreshed regularly.
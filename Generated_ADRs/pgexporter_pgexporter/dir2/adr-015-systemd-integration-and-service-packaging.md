---
### ADR-015: Systemd integration and service packaging

Status: Inferred
Context: FindSystemd.cmake, doc/etc/pgexporter.service, and RPM spec indicate first-class systemd support and distro packaging.
Decision: Provide a systemd service unit and RPM packaging for standard Linux service management and deployment.
Consequences:
- Positive: Easy integration into enterprise Linux; predictable service lifecycle management.
- Negative: Tighter coupling to systemd-based distros; additional packaging maintenance.
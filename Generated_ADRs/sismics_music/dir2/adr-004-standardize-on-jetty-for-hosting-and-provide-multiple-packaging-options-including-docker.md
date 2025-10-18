---
### ADR-004: Standardize on Jetty for hosting and provide multiple packaging options including Docker

Status: Inferred
Context: Jetty is used in agent (9.1.x) and standalone distribution (8.1.x), and Docker image is based on sismics/jetty:9.4.46. Distributions include Debian, RedHat, Windows (NSIS/Launch4j), Mac (app bundle), and standalone tar.gz.
Decision: Standardize on Jetty as the servlet container and deliver the application via multiple packaging targets (Docker, OS packages, installers, standalone).
Consequences:
- Positive: Operational flexibility; easy local/production deployments; Jetty is lightweight and embeddable; Docker image simplifies runtime dependencies (ffmpeg, youtube-dl).
- Negative: Maintaining multiple Jetty versions across modules; packaging scripts increase build complexity and CI time; additional security hardening per packaging target.
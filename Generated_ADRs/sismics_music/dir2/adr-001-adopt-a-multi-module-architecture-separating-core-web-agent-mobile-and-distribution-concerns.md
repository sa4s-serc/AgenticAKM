### ADR-001: Adopt a multi-module architecture separating core, web, agent, mobile, and distribution concerns

Status: Inferred
Context: The repository contains multiple Maven/Gradle modules: music-core (domain/services/persistence), music-web (REST/websocket APIs + web UI), music-web-common (shared web code), music-agent (desktop tray agent), music-android (native app), and several OS-specific distribution modules (Debian, RedHat, Windows, Mac, Standalone, Docker).
Decision: Structure the system as a set of cooperating modules: core business logic in music-core; HTTP APIs and web UI in music-web using music-web-common; platform packaging in dedicated distribution modules; and clients (desktop agent and Android) in separate projects.
Consequences: 
- Positive: Clear separation of concerns, independent build/release of components, easier reuse and testing (core is testable without web/app layers).
- Negative: More build complexity and inter-module dependencies; coordination required for versioning across modules.
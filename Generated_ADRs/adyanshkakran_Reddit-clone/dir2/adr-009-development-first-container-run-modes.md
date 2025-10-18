---
### ADR-009: Development-first container run modes

Status: Inferred
Context: The frontend container runs npm run dev (Vite dev server). Backend includes nodemon in dependencies, though Dockerfile uses node to start the app. Volumes mount source code into containers.
Decision: Optimize the container setup for development workflows (live-reload for the frontend; code mounted into containers; simple start commands).
Consequences:
- Positive: Fast feedback loops; minimal friction to start hacking across services.
- Negative: Dev-oriented settings may not be production-ready (e.g., no multistage builds, no asset serving from Nginx for built frontend, potential need for separate production Dockerfiles).
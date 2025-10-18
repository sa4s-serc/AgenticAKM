### ADR-001: Containerize the system and orchestrate with Docker Compose

Status: Inferred
Context: The repository includes Dockerfiles for backend, frontend, and nginx, and a top-level docker-compose.yml that defines and wires these services together with port mappings and dependencies.
Decision: Use Docker and docker-compose to containerize the backend (Node.js), frontend (React/Vite), and an Nginx reverse proxy, orchestrating them as separate services.
Consequences: 
- Positive: Reproducible environments, simplified local setup, clear service boundaries, and consistent runtime across machines.
- Negative: Increased complexity versus a single-process app, container build times, and the need to manage multiple ports and service lifecycles.
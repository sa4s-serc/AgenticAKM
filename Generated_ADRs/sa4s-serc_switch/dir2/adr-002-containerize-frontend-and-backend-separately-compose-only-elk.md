---
### ADR-002: Containerize frontend and backend separately; compose only ELK

Status: Inferred
Context: The repository contains two Dockerfiles: one at the root for a Node-based UI, and one in NAVIE/ for a Python backend. docker-compose.yml defines only Elasticsearch and Kibana services.
Decision: Build and run frontend and backend containers separately, while docker-compose manages only the ELK stack used across services.
Consequences:
- Positive: Decouples app lifecycle from observability; flexibility to run either service independently; simpler compose file.
- Negative: More manual orchestration/wiring of app services; requires consistent network/config management when integrating with ELK.
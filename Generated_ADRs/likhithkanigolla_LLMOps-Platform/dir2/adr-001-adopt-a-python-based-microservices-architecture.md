### ADR-001: Adopt a Python-based microservices architecture

Status: Inferred
Context: The repository contains multiple independently deployed services: agent-Service, controller-Service, deployer-service, model-registry, service-registry, api-gateway, reverse-proxy, vm-service, and a Flask-based frontend. Each has its own requirements and bootstrap scripts, indicating separation of concerns and autonomous deployment.
Decision: Build the system as multiple Python microservices, primarily using Flask, with one service (API Gateway) using FastAPI.
Consequences: 
- Positive: Clear separation of responsibilities; independent deployment and scaling; language consistency (Python) simplifies developer onboarding.
- Negative: Increased operational complexity (service discovery, routing, bootstrap/orchestration); potential duplication of cross-cutting concerns across services.
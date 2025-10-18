---
### ADR-011: Introduce an internal reverse-proxy service distinct from the API Gateway

Status: Inferred
Context: reverse-proxy/reverse-proxy.py exists separately from api-gateway; suggests internal routing or request fan-out distinct from public API concerns.
Decision: Maintain a Python-based reverse proxy for internal request routing, separate from the external API gateway.
Consequences:
- Positive: Separation of edge-facing concerns (auth, rate limiting) from internal routing; flexibility to evolve independently.
- Negative: Additional hop and operational component; potential duplication of routing rules.
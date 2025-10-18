# ADR-002: Production serving via Gunicorn (WSGI)

**Date**: 2025-10-14
**Status**: Proposed

## Context
requirements.txt pins gunicorn 22.0.0 and the repo is containerized for deployment.

## Decision
Run the Flask app behind Gunicorn as the production WSGI server.

## Consequences
- Proven, production-grade serving with worker/process management
- WSGI constraints (no native websockets/ASGI); async features require workarounds or different stack
- Throughput tuned via workers/threads; higher memory footprint per worker
- Operational simplicity in containerized environments
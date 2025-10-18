---
### ADR-003: Containerize with Multi-Stage Docker Build on Python 3.12-slim

Status: Inferred
Context: The Dockerfile uses a two-stage build: a “python_cache” stage to install dependencies into a virtual environment and a “build” stage that copies this venv and app code. This pattern aims to optimize build times and image size.
Decision: Use a multi-stage Docker build on python:3.12-slim, caching dependencies in a venv and copying them into the final image.
Consequences: Results in faster rebuilds and smaller runtime images. The approach is simple and effective but requires careful cache invalidation (changes to requirements.txt trigger dependency rebuilds). The image runs as root by default, which may have security implications unless further hardened.
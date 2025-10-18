---
### ADR-011: Favor lightweight base images with pinned dependencies

Status: Inferred
Context: NAVIE uses python:3.8-slim-buster with a large, pinned requirements.txt; Node image used for UI; explicit EXPOSE declarations; CMD runs Node.py in backend.
Decision: Use slim base images and tightly pinned dependencies to ensure reproducible builds and predictable runtime behavior across environments.
Consequences:
- Positive: Deterministic builds; smaller base image footprint; easier dependency auditing.
- Negative: Long install time due to heavy ML/libs; Python 3.8 is nearing/at EOL, implying future upgrade work; potential compatibility friction when updating packages.
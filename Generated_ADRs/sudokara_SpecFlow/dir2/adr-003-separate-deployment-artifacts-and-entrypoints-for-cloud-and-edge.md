---
### ADR-003: Separate deployment artifacts and entrypoints for cloud and edge

Status: Inferred
Context: There are distinct run_cloud.py and run_edge.py entrypoints, separate requirements-{cloud|edge*.txt}, and separate modules for cloud (cloud/*) and edge (edge/*). Windows setup scripts indicate different setup needs per environment.
Decision: Provide isolated deployment paths and entrypoints for the cloud server and edge client to accommodate different runtimes, dependencies, and operational concerns.
Consequences:
- Positive: Clear separation of concerns; independent packaging and scaling; tailored optimization for each environment.
- Negative: Duplicated operational overhead (version management, deployment pipelines); requires strict API compatibility management.
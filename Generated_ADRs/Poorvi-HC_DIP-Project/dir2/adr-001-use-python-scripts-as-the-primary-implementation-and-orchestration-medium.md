### ADR-001: Use Python scripts as the primary implementation and orchestration medium

Status: Inferred
Context: The repository consists entirely of .py files that implement algorithms, feature extraction, training routines, and utilities. This suggests a need for rapid prototyping and ease of iteration typical of research or exploratory engineering work.
Decision: Implement the system as a collection of Python scripts to support fast experimentation and straightforward command-line execution.
Consequences: 
- Positive: Rapid development, rich ecosystem for numerical computing and ML, low barrier to entry for contributors.
- Negative: Potential performance limits for heavy workloads, less structure than a packaged/library approach, and harder dependency/version management without explicit packaging.
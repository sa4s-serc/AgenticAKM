# ADR-005: Python-centric Stack for ML and Experimentation

**Date**: 2025-10-10
**Status**: Proposed

## Context
The project is a research-oriented proof-of-concept that heavily involves data manipulation, machine learning, and results visualization. The technology stack needed to facilitate rapid prototyping and analysis in this domain.

## Decision
The system was implemented entirely in Python, leveraging a standard data science and ML ecosystem. This includes Scikit-learn for clustering, Pandas for data manipulation, Jupyter Notebooks for analysis and visualization, and Pickle (`.pkl`) for model serialization.

## Consequences
This stack significantly accelerated development, as these tools are purpose-built for such tasks. The ecosystem provides powerful, high-level abstractions for complex operations. For a production system, some choices might be revisited; for example, Pickle has security and versioning limitations, and Python's performance for high-concurrency I/O might require an alternative like Go or Rust for the core service.
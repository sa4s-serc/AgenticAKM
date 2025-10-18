# ADR-003: Selection of a Polyglot Technology Stack (React & Python)

**Date**: 2025-10-10
**Status**: Proposed

## Context
The system's requirements span two different domains: creating a modern, interactive web interface and implementing complex backend logic with heavy data processing and machine learning integration. A single language or framework would be suboptimal for addressing both effectively.

## Decision
A polyglot approach was chosen, leveraging the strengths of different ecosystems. React (JavaScript) is used for the frontend to build a dynamic and responsive user interface. Python, with its rich data science libraries and high-performance FastAPI framework, is used for the backend control plane and ML model orchestration.

## Consequences
This strategy optimizes for both developer productivity and application performance, using the best tool for each specific job. The trade-off is increased complexity in the toolchain and a requirement for development teams to have expertise across both JavaScript and Python ecosystems.
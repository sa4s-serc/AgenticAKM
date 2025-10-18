# ADR-001: Adoption of a Managed Search Service for the Core Architecture

**Date**: 2025-10-09
**Status**: Proposed

## Context
The project required a sophisticated system to index, enrich, and query a heterogeneous collection of unstructured documents. Building the core indexing engine, document content crackers, and AI enrichment capabilities from scratch would be time-consuming, complex, and difficult to scale.

## Decision
The architecture was centered around Azure Cognitive Search, a fully managed Platform-as-a-Service (PaaS) offering. This service was chosen to handle the entire search lifecycle, from data ingestion and indexing to AI enrichment and querying.

## Consequences
This decision drastically reduced development time and operational overhead by leveraging a pre-built, scalable, and resilient search infrastructure. It provided out-of-the-box document cracking for various formats and an extensible AI enrichment pipeline. However, it also results in strong vendor lock-in to the Microsoft Azure platform and associated consumption-based costs.
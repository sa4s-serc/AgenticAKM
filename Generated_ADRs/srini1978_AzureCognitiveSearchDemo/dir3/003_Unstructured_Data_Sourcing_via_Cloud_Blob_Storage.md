# ADR-003: Unstructured Data Sourcing via Cloud Blob Storage

**Date**: 2025-10-09
**Status**: Proposed

## Context
A centralized, scalable, and reliable location was needed to store the source documents (PDFs, DOCX, images, etc.) before they could be processed by the search service.

## Decision
Azure Blob Storage was selected as the primary data source. An Azure Cognitive Search Indexer was configured to automatically monitor this storage container, triggering the indexing and enrichment pipeline whenever new documents are added.

## Consequences
This provides a cost-effective and highly durable storage solution that integrates seamlessly with Azure Cognitive Search. The indexer-based approach creates an automated, event-driven data ingestion workflow. The architecture is therefore tightly coupled to the Azure Blob Storage service; ingesting data from other sources like databases or streams would require different configurations or additional integration components.
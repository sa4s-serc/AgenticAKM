# ADR-002: Extensible Data Enrichment via Serverless Custom Skills

**Date**: 2025-10-09
**Status**: Proposed

## Context
The system needed to augment internal document data with real-time information from the public web. The standard, built-in skills in Azure Cognitive Search do not support calling arbitrary external APIs like a web search engine.

## Decision
A custom enrichment skill was implemented using a .NET Azure Function. This serverless function acts as a bridge, receiving data (e.g., extracted terms) from the Cognitive Search pipeline, calling an external API (Bing Custom Search), and returning the results to be merged into the search index.

## Consequences
This creates a highly flexible and powerful enrichment pattern, decoupling the custom logic from the search service itself. The serverless function is independently scalable and can be modified to call any API, enabling limitless enrichment possibilities. The main drawbacks are increased latency in the indexing process due to the external network calls and the introduction of an additional component to manage, monitor, and secure.
# ADR-005: Leveraging an External API for Real-time Data Augmentation

**Date**: 2025-10-09
**Status**: Proposed

## Context
To enhance the value of the internal knowledge base, the system needed to provide external context. Building a proprietary web crawler and search engine to gather this information would be prohibitively complex and expensive.

## Decision
The Bing Custom Search API was integrated as the source of external information. This allows the system to query a pre-configured slice of the web for data relevant to terms found in the source documents.

## Consequences
This decision provides immediate access to relevant, real-time web data without the overhead of managing a web crawling infrastructure. The use of a 'Custom' search instance improves the signal-to-noise ratio of the results. The system is now dependent on a third-party service, introducing external costs, potential rate limits, and a dependency on the Bing API's availability and performance.
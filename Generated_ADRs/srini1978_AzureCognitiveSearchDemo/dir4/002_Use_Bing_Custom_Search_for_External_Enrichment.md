# ADR-002: Use Bing Custom Search for External Enrichment

**Date**: 2025-10-09
**Status**: Proposed

## Context
The function wraps Bing Custom Search to enrich documents with external web search results.

## Decision
Call Bing Custom Search for each input record to retrieve and return structured web results as enrichment output.

## Consequences
Provides rich, relevant external context for indexed content, but couples the pipeline to an external paid service with quota/rate limits, latency variability, and potential relevance drift; ongoing cost management and result governance are required.
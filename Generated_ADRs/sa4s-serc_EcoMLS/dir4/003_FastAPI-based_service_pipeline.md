# ADR-003: FastAPI-based service pipeline

**Date**: 2025-10-10
**Status**: Proposed

## Context
An API layer is needed to ingest requests and run the end-to-end pipeline from preprocessing to post-processing.

## Decision
Expose the pipeline via FastAPI, orchestrated by command.sh and App.py around the processing loop and MAPE-K components.

## Consequences
Straightforward HTTP integration and Python ecosystem benefits. Potential constraints include Python/GIL performance ceilings, lifecycle management complexity, and the need for additional operational hardening for production-grade deployments.
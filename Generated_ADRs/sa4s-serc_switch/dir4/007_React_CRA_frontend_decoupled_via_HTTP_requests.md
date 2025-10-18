# ADR-007: React (CRA) frontend decoupled via HTTP requests

**Date**: 2025-10-10
**Status**: Proposed

## Context
Users need a UI to initiate runs, choose approaches, and visualize status/metrics with minimal backend coupling.

## Decision
Build a Create React App UI that communicates with the backend over HTTP using Axios.

## Consequences
Straightforward developer workflow and deployment; clear separation of presentation and control; the API contract must be stabilized; presence of server-oriented Node dependencies in package.json adds build bloat and potential attack surface if unused.
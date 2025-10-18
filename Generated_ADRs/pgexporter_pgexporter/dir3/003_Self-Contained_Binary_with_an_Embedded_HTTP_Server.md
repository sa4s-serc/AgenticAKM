# ADR-003: Self-Contained Binary with an Embedded HTTP Server

**Date**: 2025-10-16
**Status**: Proposed

## Context
To simplify deployment and reduce operational complexity, the tool needed to function as a standalone unit without external dependencies like web servers (e.g., Nginx, Apache) or language runtimes.

## Decision
Implement a lightweight, native HTTP server directly within the `pgexporter` binary. This server's sole purpose is to expose the `/metrics` endpoint for Prometheus to scrape.

## Consequences
The exporter is delivered as a single, dependency-free executable, which dramatically simplifies installation, configuration, and containerization. This reinforces the project's lean and efficient design philosophy, though the embedded server lacks the advanced features of a full-fledged web server.
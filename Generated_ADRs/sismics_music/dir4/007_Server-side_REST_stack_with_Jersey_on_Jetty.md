# ADR-007: Server-side REST stack with Jersey on Jetty

**Date**: 2025-10-14
**Status**: Proposed

## Context
Dependency management includes Jersey 2.22.x and Jetty Maven plugin, indicating a RESTful service layer.

## Decision
Expose server APIs via Jersey (JAX-RS) deployed on Jetty for development and packaging.

## Consequences
Provides a mature, modular REST framework with good ecosystem support; embedded/server plugin builds are convenient but may diverge from production app server behavior; requires careful API versioning for clients.
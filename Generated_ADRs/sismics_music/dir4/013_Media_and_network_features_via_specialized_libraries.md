# ADR-013: Media and network features via specialized libraries

**Date**: 2025-10-14
**Status**: Proposed

## Context
Libraries include jaudiotagger, weupnp, and lastfm-java.

## Decision
Leverage third-party libraries for media metadata handling, UPnP discovery, and Last.fm integration.

## Consequences
Accelerates feature delivery and interoperability; external API changes and device variability can cause brittle behavior; requires attentive dependency updates and graceful failure handling.
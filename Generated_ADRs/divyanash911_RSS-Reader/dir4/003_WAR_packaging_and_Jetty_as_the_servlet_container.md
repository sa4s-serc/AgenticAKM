# ADR-003: WAR packaging and Jetty as the servlet container

**Date**: 2025-10-13
**Status**: Proposed

## Context
Build plugins support WAR packaging and a Jetty context descriptor (reader.xml) deploys reader.war at context root "/".

## Decision
Package the application as a standard WAR and deploy it on Jetty with the root context path.

## Consequences
Enables conventional servlet deployment and portability across servlet containers; simplifies reverse-proxy configuration due to root context; introduces container-specific operational considerations; imposes a WAR build step and servlet API constraints.
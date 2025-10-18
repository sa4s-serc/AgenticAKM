# ADR-002: Embedded Jetty as the Application Server

**Date**: 2025-10-13
**Status**: Proposed

## Context
The application needed a simple, self-contained deployment model that would not require users or developers to pre-configure a separate, heavyweight application server like Tomcat or JBoss.

## Decision
To use an embedded Jetty server, configured directly within the Maven build process and launched as part of the application's startup. This creates a single, executable artifact (`.war` deployed within a pre-configured server).

## Consequences
This decision greatly simplifies the development and deployment lifecycle, as the application is entirely self-sufficient. However, it tightly couples the application to a specific web server (Jetty), making it more difficult to migrate to a different server environment if future requirements change.
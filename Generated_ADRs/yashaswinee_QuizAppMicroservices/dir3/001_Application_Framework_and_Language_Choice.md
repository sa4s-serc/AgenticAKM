# ADR-001: Application Framework and Language Choice

**Date**: 2025-10-16
**Status**: Proposed

## Context
The project required a modern, robust, and highly productive backend framework for building a RESTful API using the Java language, aiming for rapid development and a rich ecosystem.

## Decision
The Spring Boot framework (version 3.5.0) was selected, built upon Java 21. This choice leverages Spring's comprehensive ecosystem for web, persistence, and dependency injection.

## Consequences
This decision enables rapid development through convention-over-configuration, an embedded web server, and simplified dependency management. It also positions the project to use modern Java 21 features. The tight integration with Spring Data JPA and Spring Web streamlines the implementation of the layered architecture.
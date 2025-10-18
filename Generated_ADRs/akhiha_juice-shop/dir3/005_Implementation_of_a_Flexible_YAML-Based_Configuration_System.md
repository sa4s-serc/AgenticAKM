# ADR-005: Implementation of a Flexible, YAML-Based Configuration System

**Date**: 2025-10-10
**Status**: Proposed

## Context
The application must support various operational modes and scenarios, such as standard training, Capture The Flag (CTF) events, and tutorials. These scenarios require different challenges, branding, and application behaviors.

## Decision
A highly flexible configuration system was built using a set of cascading YAML files. Loading a specific configuration file (e.g., `ctf.yml`) at startup alters the application's entire feature set and behavior without any code changes.

## Consequences
This provides immense versatility, allowing event organizers to easily customize the application. YAML is human-readable and easy to modify. The negative consequence is a slight increase in complexity for operators, who must understand the configuration file structure and precedence rules.
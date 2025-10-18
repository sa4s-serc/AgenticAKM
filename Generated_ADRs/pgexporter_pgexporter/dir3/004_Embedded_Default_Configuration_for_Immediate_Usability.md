# ADR-004: Embedded Default Configuration for Immediate Usability

**Date**: 2025-10-16
**Status**: Proposed

## Context
New users often face a steep learning curve when setting up monitoring tools, which typically require creating a configuration file from scratch. This initial friction can hinder adoption.

## Decision
A comprehensive, default set of standard metric queries is embedded directly into the application binary. This internal configuration is used automatically if no external file is specified.

## Consequences
This significantly lowers the barrier to entry, as the exporter provides a rich set of useful metrics immediately upon startup. It makes the tool instantly valuable for evaluation and provides users with a solid, working template for future customization.
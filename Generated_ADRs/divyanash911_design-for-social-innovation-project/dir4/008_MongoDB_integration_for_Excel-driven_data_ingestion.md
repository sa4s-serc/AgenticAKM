# ADR-008: MongoDB integration for Excel-driven data ingestion

**Date**: 2025-10-13
**Status**: Proposed

## Context
scripts/ contains excel_to_mongo_*.py scripts that load Excel data into MongoDB.

## Decision
Use MongoDB as a target for data import/transformation workflows originating from Excel sources.

## Consequences
Flexible schema suits questionnaire-like data and rapid ingestion from spreadsheets, but introduces an additional datastore to operate and align with the app’s data model; primary datastore status remains to be verified.
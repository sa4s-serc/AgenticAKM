# ADR-006: Adoption of `android-query` for Asynchronous Operations

**Date**: 2025-10-14
**Status**: Proposed

## Context
The Android application must perform network calls to the server to fetch data without freezing the user interface, which requires handling asynchronous operations.

## Decision
The `android-query` library was integrated to simplify asynchronous tasks and UI updates, abstracting away some of the complexity of Android's native threading models.

## Consequences
This library reduced boilerplate code at the time of development, making the codebase cleaner than using raw `AsyncTask`. However, `android-query` is now largely superseded by more modern solutions like Retrofit, Kotlin Coroutines, or RxJava. This choice indicates the project's age and may represent technical debt that complicates future maintenance.
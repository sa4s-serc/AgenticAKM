---
### ADR-003: Multi-Paradigm Asynchronous Support via Modular Extensions

**Status:** Inferred

**Context:** The Swift ecosystem does not have a single, universally adopted framework for asynchronous programming. At various times, Apple's Combine, third-party libraries like RxSwift and ReactiveSwift, and traditional completion handlers have all been popular choices. A networking library that forces users into one specific paradigm risks alienating a significant portion of its potential user base.

**Decision:** The core library (`Moya`) was designed to be dependency-free and based on simple completion handlers. To support popular reactive frameworks, separate, optional sub-modules were created: `RxMoya`, `ReactiveMoya`, and `CombineMoya`. Each module provides extension methods on `MoyaProvider` that expose the library's functionality through that framework's specific primitives (e.g., `Observable` for RxSwift, `SignalProducer` for ReactiveSwift, `Publisher` for Combine).

**Consequences:**
*   **Positive:**
    *   **Broad Adoption:** Developers can integrate the library into their existing architecture regardless of which asynchronous framework they use.
    *   **Lean Core:** The core `Moya` module remains lightweight and does not impose any third-party dependencies on users who don't need them.
    *   **Clear Separation:** The logic for each reactive extension is isolated in its own module, making it easier to maintain and update independently.
*   **Negative:**
    *   **Increased Maintenance Overhead:** The project maintainers must support and test multiple modules and their integrations with different versions of the reactive frameworks.
    *   **Slightly More Complex Setup:** Users need to explicitly include the specific extension module for the framework they want to use.
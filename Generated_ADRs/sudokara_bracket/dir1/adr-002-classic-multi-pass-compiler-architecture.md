---
### ADR-002: Classic Multi-Pass Compiler Architecture

**Status:** Inferred

**Context:** Compiling a source language (Racket, based on `.rkt` files) into a lower-level representation requires a systematic process to manage complexity. The process involves transforming source text through several stages of analysis and translation. A monolithic approach would be difficult to develop, debug, and maintain.

**Decision:** The compiler is architected as a traditional multi-pass pipeline. The file structure clearly delineates these distinct phases:
1.  **Lexer (`Lexer/`):** Scans the source code and converts it into a stream of tokens.
2.  **Parser (`Parser/`):** Consumes the token stream to build an Abstract Syntax Tree (AST).
3.  **AST (`AST/`):** Defines the core data structures for representing the code's structure.
4.  **Sema (`Sema/`):** Performs Semantic Analysis on the AST, handling tasks like type checking and scope resolution.
5.  **CodeGen (`CodeGen/`):** Traverses the validated AST to generate the final target code (likely LLVM IR, given the `LL` prefix in `llracket`).

**Consequences:**
*   **Positive:**
    *   **Separation of Concerns:** Each compiler stage has a well-defined responsibility, making the overall system easier to reason about, develop, and test independently.
    *   **Maintainability:** Bugs can be more easily isolated to a specific stage (e.g., a syntax error is a Parser issue, a type mismatch is a Sema issue).
    *   **Extensibility:** New language features or target architectures can be added by modifying or extending specific passes without rewriting the entire compiler.
*   **Negative:**
    *   **Performance Overhead:** Each pass requires traversing the AST or an intermediate representation, which can be less performant than a single-pass compiler.
    *   **Data Structure Overhead:** Requires well-defined data structures (Tokens, AST) to pass information between stages, adding some boilerplate code.
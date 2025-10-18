# ADR-002: Adoption of a Pratt Parser

**Date**: 2025-10-11
**Status**: Proposed

## Context
The language includes expressions with various operators that have different precedence levels (e.g., multiplication before addition). The parser needed an efficient and clean way to handle these rules when constructing the AST.

## Decision
A Pratt parsing algorithm was chosen and implemented. This technique associates parsing functions with token types, elegantly handling operator precedence and associativity with a non-recursive, table-driven approach.

## Consequences
This is a sophisticated choice that leads to a cleaner and more efficient parser compared to more verbose methods like recursive descent with manual precedence climbing. It simplifies the logic required to correctly parse complex expressions, making the parser code more readable and maintainable.
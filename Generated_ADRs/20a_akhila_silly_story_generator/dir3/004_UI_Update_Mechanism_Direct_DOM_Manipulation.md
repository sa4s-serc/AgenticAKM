# ADR-004: UI Update Mechanism: Direct DOM Manipulation

**Date**: 2025-10-10
**Status**: Proposed

## Context
After the user provides input and initiates the story generation, the application's UI must be updated to display the output. The method for updating the view needed to be defined.

## Decision
To use JavaScript to directly manipulate the Document Object Model (DOM). The script programmatically finds the designated placeholder paragraph, updates its text content with the generated story, and modifies its CSS `visibility` property to make it appear.

## Consequences
This approach is very direct, efficient, and sufficient for simple applications. It avoids the overhead of a virtual DOM or a complex state management library. In a larger application with more dynamic data and components, this method could become complex, error-prone, and lead to performance bottlenecks and less maintainable code.